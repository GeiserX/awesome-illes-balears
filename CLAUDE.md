# CLAUDE.md — awesome-illes-balears

## Propósito

Selección de software open source que da **soporte específico a les Illes Balears** — su govern autonòmic (CAIB), consells insulars, ajuntaments, universitat, empresas, infraestructuras y patrimonio. Todo el contenido en español. El foco es les Illes Balears: el software debe dirigirse específicamente a esta comunidad autónoma o a sus islas y municipios.

## Ámbito

- **4 islas principales**: Mallorca, Menorca, Eivissa (Ibiza), Formentera.
- Principales ciudades: Palma (capital), Inca, Manacor, Llucmajor, Marratxí, Calvià, Maó (Mahón), Ciutadella de Menorca, Eivissa (ciudad), Sant Antoni de Portmany, Santa Eulària des Riu, Sant Josep de sa Talaia, Formentera (Sant Francesc Xavier).
- **Universidades**: UIB (Universitat de les Illes Balears).
- **Instituciones**: CAIB (Govern de les Illes Balears / GovernIB), Consells Insulars (Mallorca, Menorca, Eivissa, Formentera), SOCIB (Sistema d'Observació i Predicció Costaner de les Illes Balears), IB-Salut (Servei de Salut de les Illes Balears), IBANAT, ATB (Autoritat de Transport Metropolità de Mallorca).

## Criterios de inclusión

### Incluir

- Software que interactúa con el **CAIB / GovernIB** o sus organismos (Sede Electrónica, Portal de Transparencia, datos abiertos).
- Herramientas para **ajuntaments** o **consells insulars** de les Illes Balears.
- Software de la **UIB** (Universitat de les Illes Balears) cuando sea específico de la región o la universidad.
- Software de **SOCIB** (oceanografía costera balear).
- Herramientas de **datos abiertos** de les Illes Balears.
- Software relacionado con el **transporte** balear (TIB, EMT Palma, buses interurbanos, transporte marítimo interinsular).
- Herramientas de **medio ambiente y mar** de les Illes Balears.
- Software de **turismo** específico de las islas.
- Herramientas de **cartografía y SIG** específicas de les Illes Balears (IDEIB, Infraestructura de Dades Espacials).
- Software sobre **playas y costa** balear.
- Proyectos del **sistema sanitario balear** (IB-Salut).
- Software **educativo** específico de la región.

### No incluir

- Software **genérico** que funciona en toda España sin funcionalidad específica de les Illes Balears — eso pertenece a awesome-spain.
- Software de **ámbito europeo** — eso pertenece a awesome-europe.
- Software de **otras comunidades autónomas** españolas.
- Software creado por baleares que **no tiene funcionalidad específica** de la región.
- Repositorios **archivados o de solo lectura** — van a `DELETED.md`.
- Repos donde el autor indica que el proyecto está **roto, sin mantenimiento o deprecado**.
- Repos **sin README significativo** o que son claramente repos de test/experimento.
- Ejercicios de clase o trabajos académicos sin utilidad real.

### Zona gris — usar criterio

- Proyectos de la UIB que podrían ser genéricos — incluir si tienen datos o configuración específica de les Illes Balears.
- Software que cubre les Illes Balears junto con otras regiones — incluir si les Illes Balears es un foco principal.

## Estándares de calidad

**Mismo listón que [awesome-spain](https://github.com/GeiserX/awesome-spain):**

- **No repos archivados**: si se descubre archivado tras la inclusión, mover a `DELETED.md` inmediatamente.
- **No repos extremadamente sin mantenimiento**: al menos un commit en los últimos 3 años, salvo que sea un proyecto claramente estable/completo.
- **No repos rotos**: si el README dice «deprecated», «no longer maintained», «use X instead» o similar — no incluir. Mover a `DELETED.md` si ya está listado.
- **Estrellas mínimas**: preferir repos con al menos unas pocas estrellas, pero herramientas nicho excepcionales con 0-1 estrellas pueden incluirse si cubren un hueco importante.
- **Verificar cada repo** antes de añadir: comprobar `archived`, `pushed_at`, `stargazers_count` vía `gh api repos/owner/name`.

## Formato de entrada

```markdown
- [Nombre](https://github.com/owner/repo) [![Stars](...)](stargazers) [![Last Commit](...)](commits) [![Language](...)](repo) [![License](...)](LICENSE) [![Tag](...)](url) - Descripción que empieza en mayúscula y termina con punto.
```

Las insignias se generan automáticamente con `scripts/transform-readme.py`. Para contribuir, basta con añadir la entrada en formato simple:

```markdown
- [Nombre](https://github.com/owner/repo) - Descripción que empieza en mayúscula y termina con punto.
```

- La descripción **no debe empezar con el nombre** del proyecto.
- Máximo una línea por entrada.
- Validar con awesome-lint-extra: `python3 lint.py` o mediante el workflow de CI.
- Entradas en **orden alfabético** dentro de cada categoría.
- Categorías en **orden alfabético** en el índice y en el cuerpo del documento.
- Entradas en `DELETED.md` también en **orden alfabético** dentro de cada sección.

## Verificación antes de añadir

Antes de incluir un repositorio, comprobar:

- **Existe y es público**: el enlace de GitHub funciona y el repo no es privado.
- **No está archivado o de solo lectura**: si archivado, va a `DELETED.md` (sección «Archivados»).
- **No está deprecado**: comprobar si el README dice «deprecated», «unmaintained», «broken», «use X instead».
- **Actividad razonable**: al menos un commit en los últimos 3 años, salvo que sea un proyecto estable/completo.
- **No es un duplicado**: cruzar con `README.md` y `DELETED.md`.
- **Calidad mínima**: tiene documentación (README) y no es un repositorio vacío o de test.

## Pull requests y contribuciones

- Las PRs deben usar la plantilla en `.github/PULL_REQUEST_TEMPLATE.md`.
- **Obligatorio**: incluir en la PR la **URL del servicio, API o institución balear** a la que el software da soporte.
- Plantillas de issues disponibles para sugerir proyectos (`anadir-proyecto.md`) y solicitar retirada (`retirar-proyecto.md`).

## Estructura

- Secciones con `##`, subsecciones con `###`.
- Índice de contenido al principio entre comentarios `<!--lint disable/enable awesome-list-item-->`.
- Al final: sección Contribuir, Nota y Descargo de responsabilidad (como párrafos en negrita, no encabezados ##).

## Temas prohibidos

No se aceptan proyectos relacionados con: pornografía, contenido NSFW, loterías o apuestas, religión, política partidista.

## Difusión

- Notificar a los propietarios de repos abriendo un issue titulado «Listado en awesome-illes-balears» con un breve mensaje en español (tuteo) ofreciendo retirar si lo prefieren. Solo 1 issue por organización/usuario — no spamear repos del mismo propietario.
- Publicar en comunidades baleares (Reddit, foros de la UIB, Telegram de devs baleares) tras alcanzar masa crítica.
- Enviar PR a [sindresorhus/awesome](https://github.com/sindresorhus/awesome) tras 30 días desde la creación del repo.

## Aprendizajes

- GovernIB es la organización GitHub del Govern de les Illes Balears con 58+ repos públicos. Los principales tienen 3-8 estrellas.
- La mayoría de repos GovernIB no tienen campo `language` detectable (código en submódulos o sin extensión reconocida).
- open-transport-mallorca tiene 2 repos útiles: ViaMallorca (11 estrellas, Dart) y mallorca_transit_services (5 estrellas, Dart).
- SOCIB (Sistema d'Observació Costaner) tiene repos de oceanografía con datos específicos de Baleares. Leaflet.TimeDimension (450 estrellas) es genérico, no incluir. glider_toolbox (40 estrellas) y API_examples (8 estrellas) son específicos.
- socib/grumers es una app Django para avistamientos de medusas en catalán balear — muy específico.
- Las búsquedas por "UIB" devuelven mucho ruido (University of Bergen, UI Bootstrap, etc.). Filtrar cuidadosamente.
- Las búsquedas por "ibiza" devuelven mucho ruido (música, clubbing, nombres genéricos). Filtrar cuidadosamente.
- La UIB no tiene organización oficial en GitHub con repos significativos.

---

*Bootstrapped with [LynxPrompt](https://lynxprompt.com)*

<!-- BEGIN BEADS INTEGRATION v:1 profile:minimal hash:6cd5cc61 -->
## Beads Issue Tracker

This project uses **bd (beads)** for issue tracking. Run `bd prime` to see full workflow context and commands.

### Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --claim  # Claim work
bd close <id>         # Complete work
```

### Rules

- Use `bd` for ALL task tracking — do NOT use TodoWrite, TaskCreate, or markdown TODO lists
- Run `bd prime` for detailed command reference and session close protocol
- Use `bd remember` for persistent knowledge — do NOT use MEMORY.md files

**Architecture in one line:** issues live in a local Dolt DB; sync uses `refs/dolt/data` on your git remote; `.beads/issues.jsonl` is a passive export. See https://github.com/gastownhall/beads/blob/main/docs/SYNC_CONCEPTS.md for details and anti-patterns.

## Agent Context Profiles

The managed Beads block is task-tracking guidance, not permission to override repository, user, or orchestrator instructions.

- **Conservative (default)**: Use `bd` for task tracking. Do not run git commits, git pushes, or Dolt remote sync unless explicitly asked. At handoff, report changed files, validation, and suggested next commands.
- **Minimal**: Keep tool instruction files as pointers to `bd prime`; use the same conservative git policy unless active instructions say otherwise.
- **Team-maintainer**: Only when the repository explicitly opts in, agents may close beads, run quality gates, commit, and push as part of session close. A current "do not commit" or "do not push" instruction still wins.

## Session Completion

This protocol applies when ending a Beads implementation workflow. It is subordinate to explicit user, repository, and orchestrator instructions.

1. **File issues for remaining work** - Create beads for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **Handle git/sync by active profile**:
   ```bash
   # Conservative/minimal/default: report status and proposed commands; wait for approval.
   git status

   # Team-maintainer opt-in only, unless current instructions forbid it:
   git pull --rebase
   git push
   git status
   ```
5. **Hand off** - Summarize changes, validation, issue status, and any blocked sync/commit/push step

**Critical rules:**
- Explicit user or orchestrator instructions override this Beads block.
- Do not commit or push without clear authority from the active profile or the current user request.
- If a required sync or push is blocked, stop and report the exact command and error.
<!-- END BEADS INTEGRATION -->

## Where the tracker syncs

This repo is public, so its tracker syncs only to the private Dolt remote named by `sync.remote` in `.beads/config.yaml` (`giteaer/awesome-illes-balears-beads` on Gitea). The block above says sync uses "your git remote". Here that never means this GitHub repo. Don't add it as a Dolt remote and don't push `refs/dolt/*` to it.
