"""Markdown extension: number repeated headings the way GitHub does.

The README has two `### Mallorca` headings, and its Contenido list links the
second one as #mallorca-1, the id GitHub gives it. Python-Markdown's toc would
call it mallorca_1, so on the site that link would land nowhere. Zensical does
not check anchors in text that comes in through the README include, so a
strict build stays green while the link is dead: this extension is the fix,
and awesome_site.py is the shared one that does the counts.

Runs just before toc (priority 5), which keeps an id that is already set and
slugifies the rest, so first occurrences keep toc's own id. The slugify here
must match the toc entry in zensical.toml.
"""

from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor
from pymdownx.slugs import slugify

SLUGIFY = slugify(case="lower")


class _GitHubRepeatedIds(Treeprocessor):
    def run(self, root):
        seen = {}
        for el in root.iter():
            if el.tag not in ("h1", "h2", "h3", "h4", "h5", "h6") or "id" in el.attrib:
                continue
            slug = SLUGIFY("".join(el.itertext()).strip(), "-")
            if slug in seen:
                seen[slug] += 1
                el.set("id", f"{slug}-{seen[slug]}")
            else:
                seen[slug] = 0


class GitHubRepeatedIdsExtension(Extension):
    def extendMarkdown(self, md):
        md.treeprocessors.register(_GitHubRepeatedIds(md), "aw_repeated_ids", 6)


def makeExtension(**kwargs):
    return GitHubRepeatedIdsExtension(**kwargs)
