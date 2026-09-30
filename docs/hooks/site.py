"""MkDocs hooks for the one-page site.

on_page_markdown replaces the `<!-- n:... -->` tokens in docs/index.md with
numbers counted from README.md and DELETED.md at build time, so the home page
never states a stale figure. Entries are counted inside category sections
only: a `## Mantenedores` list of GitHub profiles is not a project.

on_page_content adds loading="lazy" to every image except the banner, so a
page with hundreds of shields.io badges paints before they all arrive, and
fails the build if the list did not come through the include. A missing
section marker already fails the build in pymdownx.snippets (check_paths:
true raises SnippetMissingError); this check is for markers that exist but
enclose the wrong lines.

on_config gives a repeated heading the id GitHub gives it. The README has two
`### Mallorca` headings and its Contenido links the second as #mallorca-1, as
GitHub numbers it; Python-Markdown's toc would call it mallorca_1 and the
strict build would fail on the missing anchor.
"""

import re
from pathlib import Path

from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor

ROOT = Path(__file__).resolve().parents[2]
ENTRY = re.compile(r"^- \[[^\]]+\]\(https?://")
# DELETED.md also lists repos that no longer exist as "- `owner/repo` - reason", with no link:
# they are retired projects too and count as such.
RETIRED = re.compile(r"^- (?:\[[^\]]+\]\(https?://|`[^`]+` - )")
H2 = re.compile(r"^## (.+)$")
NOT_CATEGORIES = {
    "Contenido",
    "Insignia",
    "Mantenedores",
    "Contribuir",
    "Nota",
    "Descargo de responsabilidad",
}
IMG = re.compile(r"<img\b[^>]*>")
LISTED = re.compile(r"<li>\s*<a href=\"https?://")


class _GitHubRepeatedIds(Treeprocessor):
    """Number repeated headings like GitHub: mallorca, mallorca-1, mallorca-2.

    Runs just before toc (priority 5), which keeps an id that is already set
    and slugifies the rest, so first occurrences keep toc's own id.
    """

    def __init__(self, md, slugify):
        super().__init__(md)
        self.slugify = slugify

    def run(self, root):
        seen = {}
        for el in root.iter():
            if el.tag not in ("h1", "h2", "h3", "h4", "h5", "h6") or "id" in el.attrib:
                continue
            slug = self.slugify("".join(el.itertext()).strip(), "-")
            if slug in seen:
                seen[slug] += 1
                el.set("id", f"{slug}-{seen[slug]}")
            else:
                seen[slug] = 0


class _GitHubRepeatedIdsExtension(Extension):
    def __init__(self, slugify):
        super().__init__()
        self.slugify = slugify

    def extendMarkdown(self, md):
        md.treeprocessors.register(_GitHubRepeatedIds(md, self.slugify), "aw_repeated_ids", 6)


def on_config(config):
    config.markdown_extensions.append(_GitHubRepeatedIdsExtension(config.mdx_configs["toc"]["slugify"]))
    return config


def _entries_by_section(text):
    """Yield (section title or None, is_entry) for every line."""
    section = None
    for line in text.splitlines():
        heading = H2.match(line)
        if heading:
            section = heading.group(1).strip()
            continue
        yield section, bool(ENTRY.match(line))


def _counts():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    deleted = (ROOT / "DELETED.md").read_text(encoding="utf-8")
    categories = set()
    proyectos = 0
    for section, is_entry in _entries_by_section(readme):
        if section is None or section in NOT_CATEGORIES:
            continue
        categories.add(section)
        proyectos += is_entry
    return {
        "proyectos": proyectos,
        "categorias": len(categories),
        "retirados": sum(1 for line in deleted.splitlines() if RETIRED.match(line)),
    }


def on_page_markdown(markdown, page, config, files):
    if page.file.src_uri != "index.md":
        return markdown
    for key, value in _counts().items():
        markdown = markdown.replace(f"<!-- n:{key} -->", str(value))
    if "<!-- n:" in markdown:
        raise RuntimeError("docs/index.md has a count token the hook does not know")
    return markdown


def on_page_content(html, page, config, files):
    if page.file.src_uri != "index.md":
        return html
    listed = len(LISTED.findall(html))
    expected = _counts()["proyectos"]
    if 'id="contenido"' not in html or 'id="insignia"' not in html or listed < expected:
        raise RuntimeError(
            f"docs/index.md shows {listed} of the README's {expected} projects: "
            "check the `--8<-- [start:lista]` and `[end:lista]` markers in README.md"
        )

    def lazy(match):
        tag = match.group(0)
        if "banner.svg" in tag or "loading=" in tag:
            return tag
        return tag.replace("<img", '<img loading="lazy" decoding="async"', 1)

    return IMG.sub(lazy, html)
