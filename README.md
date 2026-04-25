# DSFR · `DESIGN.md`

A `DESIGN.md` encoding of the **Système de Design de l'État Français** (DSFR) for AI coding agents.

This repository publishes a single source-of-truth `DESIGN.md` file that translates the official French government design system — colours, typography, spacing, and core component patterns — into the **open `DESIGN.md` format** specified by Google Stitch ([`google-labs-code/design.md`](https://github.com/google-labs-code/design.md)).

The goal is simple: **let any DESIGN.md-aware coding agent (Stitch, Claude Code, Cursor, Kiro, Windsurf, Letta Code, …) generate UIs that look and behave like a `.gouv.fr` site by default.**

---

## Why this exists

The DSFR is the [mandatory design system](https://www.systeme-de-design.gouv.fr/version-courante/fr/a-propos/articles-et-actualites/circulaire-d-application-du-7-juillet-2023) for French State web services (circulaire n°6411-SG). It ships as `@gouvfr/dsfr` on npm — a complete HTML/CSS/JS toolkit with 50+ accessible components — but coding agents that generate UI from natural-language prompts don't read SCSS files.

The Stitch `DESIGN.md` format was designed specifically for this gap: a hybrid YAML-front-matter + Markdown document that gives agents a **persistent, structured understanding of a design system**, validatable against WCAG via `npx @google/design.md lint`.

This project bridges the two.

---

## What's in the box

```
.
├── DESIGN.md          ← the design system, in DESIGN.md format
├── README.md          ← this file
└── .gitignore
```

The `DESIGN.md` covers:

| Layer | Content |
|-------|---------|
| **YAML front matter** | Bleu France & Rouge Marianne option tokens, neutrals, system (success/warning/error/info), illustrative accents (12 families), decision tokens, Marianne & Spectral typography scale, `v`-based spacing scale, border-radius scale, ~15 core components (buttons, inputs, select, checkbox, radio, toggle, card, tile, tag, alert, badge, modal, breadcrumb, callout, header/footer) with hover/active/focus/disabled state variants. |
| **Markdown body** | 8 canonical sections — Overview · Colors · Typography · Layout · Elevation & Depth · Shapes · Components · Do's and Don'ts — explaining the *why* behind every value, including DSFR-specific rules like "never apply Bleu France to titles" and the `data-fr-scheme` light/dark mechanism. |

The file targets the **light theme**. Dark-theme decision-token mappings are documented in prose because the alpha `DESIGN.md` spec doesn't have first-class theme switching.

---

## Usage

### Import into Google Stitch

1. Open your Stitch project.
2. **Settings → Design System → Import DESIGN.md**.
3. Paste the file contents (or upload).
4. Generate prompts as usual — Stitch will apply DSFR colours, typography, square corners, and component patterns automatically.

### Use with other coding agents

Drop `DESIGN.md` at the root of your project. Most modern agents (Claude Code, Cursor, Kiro, Windsurf, Letta Code) will pick it up as design context. Some agents accept a `--design-md` flag; consult their docs.

### Lint and validate

```bash
npx @google/design.md lint DESIGN.md
```

This checks for broken token references, missing primary colour, contrast-ratio violations against WCAG AA (4.5:1), orphaned tokens, and section ordering.

**Expected lint output**: `0 errors, ≈41 warnings, 1 info` — every warning is an `orphaned-tokens` finding and is intentional:

- The 16 **illustrative-palette** colours (tilleul-verveine, glycine, tournesol, etc.) are accent-only by DSFR rule; they must not be referenced from buttons or system components.
- The raw **option tokens** (e.g. `blue-france-main-525`, `red-marianne-*`) are kept as a documentation reference layer. UI code is supposed to consume the **decision tokens** that point at them — those *are* referenced by components.
- `focus-ring` and `border-default-grey` would require component properties (`outline`, `borderColor`) that the alpha `DESIGN.md` spec doesn't yet define.

Should the spec gain those properties in a future version, this file should be updated to wire the orphans through.

### Export to other formats

```bash
# Tailwind theme
npx @google/design.md export --format tailwind DESIGN.md > tailwind.theme.json

# W3C DTCG tokens.json
npx @google/design.md export --format dtcg     DESIGN.md > tokens.json
```

---

## Important caveats

### ⚠️ Legal & brand scope

The DSFR's visual identity — the Marianne wordmark, the *République Française* logo, the Bleu France colour used as a state mark, and the Marianne typeface — is **legally restricted to official French State websites and applications**. Per the DSFR's terms of use:

> Il est formellement interdit à tout autre acteur d'utiliser le Système de Design de l'État (les administrations territoriales ou tout autre acteur privé) pour des sites web ou des applications.

This `DESIGN.md` is a **derived, machine-readable description** of the design system, useful for:

- ✅ State teams (`.gouv.fr` services) building with AI agents.
- ✅ Educational and research purposes.
- ✅ Prototyping internal tools that will eventually use the canonical `@gouvfr/dsfr` package.

It is **not** a licence to brand third-party services as governmental. Use the official `@gouvfr/dsfr` npm package for any production .gouv.fr build.

### ⚠️ Spec is alpha

The Stitch `DESIGN.md` format is currently at version `alpha`. Token schema and CLI behaviour may change. Pin a specific `@google/design.md` version in any automated pipeline.

### ⚠️ Lossy encoding

The DSFR is richer than the alpha spec can represent — option-token granularity, decision tokens, dual-theme switching, illustrative palettes, RGAA-specific accessibility rules. We capture the essentials in YAML and document the rest in prose. For canonical fidelity, always defer to:

- **Source of truth (visual)**: <https://www.systeme-de-design.gouv.fr/version-courante/fr>
- **Source of truth (code)**: [`@gouvfr/dsfr`](https://www.npmjs.com/package/@gouvfr/dsfr) — `node_modules/@gouvfr/dsfr/dist/core/colors.json`

---

## Sources & references

- DSFR documentation — <https://www.systeme-de-design.gouv.fr>
- DSFR repository — <https://github.com/GouvernementFR/dsfr>
- `DESIGN.md` specification — <https://github.com/google-labs-code/design.md>
- Stitch announcement — <https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-design-md/>
- W3C Design Tokens Format Module — <https://tr.designtokens.org/format/>

---

## Licence

The `DESIGN.md` content in this repository is published under **MIT** (matching the DSFR's source-code licence) **with the explicit caveat above** about the visual identity. The Marianne typeface itself is **not** redistributed here — refer to the [DSFR LICENSE.md](https://github.com/GouvernementFR/dsfr/blob/main/LICENSE.md) for typeface terms.
