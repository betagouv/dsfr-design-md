---
version: alpha
name: DSFR — Système de Design de l'État
description: >
  Design tokens and component patterns derived from the official French
  government design system (DSFR v1.14, https://www.systeme-de-design.gouv.fr).
  Encodes the Bleu France / Rouge Marianne brand identity, Marianne & Spectral
  typography, the v-based spacing scale, and core component decision tokens
  for the LIGHT theme. Components follow BEM (`fr-*` classes) and target
  RGAA / WCAG 2.1 AA compliance. Dark-theme mappings are documented in prose.

colors:
  # ============================================================
  # OPTION TOKENS — raw palette, indexed by hue/family
  # ============================================================
  # These mirror the DSFR token names of the form
  #   COULEUR-NOM-VARIANTE-INDICE-ÉTAT
  # so they can be grepped against the official documentation.

  # ---------- Brand: Bleu France ----------
  blue-france-sun-113-625:        "#000091"
  blue-france-sun-113-625-hover:  "#1212ff"
  blue-france-sun-113-625-active: "#2323ff"
  blue-france-main-525:           "#6a6af4"
  blue-france-850-200:            "#cacafb"
  blue-france-925-125:            "#e3e3fd"
  blue-france-925-125-hover:      "#c1c1fb"
  blue-france-925-125-active:     "#adadf9"
  blue-france-950-100:            "#ececfe"
  blue-france-950-100-hover:      "#cecefc"
  blue-france-950-100-active:     "#bbbbfc"
  blue-france-975-75:             "#f5f5fe"
  blue-france-975-75-hover:       "#dcdcfc"
  blue-france-975-75-active:      "#cbcbfa"

  # ---------- Brand: Rouge Marianne ----------
  red-marianne-425-625:           "#c9191e"
  red-marianne-425-625-hover:     "#f93f42"
  red-marianne-425-625-active:    "#f95a5c"
  red-marianne-main-472:          "#e1000f"
  red-marianne-850-200:           "#fcbfbf"
  red-marianne-925-125:           "#fddede"
  red-marianne-925-125-hover:     "#fbb6b6"
  red-marianne-925-125-active:    "#fa9e9e"
  red-marianne-950-100:           "#fee9e9"
  red-marianne-950-100-hover:     "#fdc5c5"
  red-marianne-950-100-active:    "#fcafaf"
  red-marianne-975-75:            "#fef4f4"
  red-marianne-975-75-hover:      "#fcd7d7"
  red-marianne-975-75-active:     "#fac4c4"

  # ---------- Neutrals (greys) — light-theme orientation ----------
  # As with the brand colours, the DSFR ships hover/active states only
  # for the grey shades intended as interactive surfaces (white surface,
  # tinted backgrounds, action-text). Borders, body text, mention text,
  # absolute black/white and the docs-only `main` and `850-200` shades
  # are static — they have no hover/active in the canonical CSS.
  grey-main-525:                  "#7b7b7b"
  grey-1000-50:                   "#ffffff"
  grey-1000-50-hover:             "#f6f6f6"
  grey-1000-50-active:            "#ededed"
  grey-975-100:                   "#f6f6f6"
  grey-975-100-hover:             "#dfdfdf"
  grey-975-100-active:            "#cfcfcf"
  grey-950-150:                   "#eeeeee"
  grey-950-150-hover:             "#d2d2d2"
  grey-950-150-active:            "#c1c1c1"
  grey-925-125:                   "#e5e5e5"
  grey-900-175:                   "#dddddd"
  grey-850-200:                   "#cecece"
  grey-625-425:                   "#929292"
  grey-425-625:                   "#666666"
  grey-200-850:                   "#3a3a3a"
  grey-200-850-hover:             "#616161"
  grey-200-850-active:            "#777777"
  grey-50-1000:                   "#161616"
  grey-0-1000:                    "#000000"

  # ---------- System (functional) ----------
  # Family order is fixed by the DSFR docs:
  # « Les couleurs systèmes sont : Info, warning, error, success. »
  #
  # Each family exposes 6 shades following the same convention as the
  # brand colours (main → strong → lightest → lighter → light → softest):
  #   - `-main-525` reference value (theme-stable, both themes use the
  #                 same hex). Documented in DSFR but NOT exposed as a
  #                 CSS variable in `dsfr.css`. Same category as
  #                 `blue-france-main-525`, `grey-main-525`, etc.
  #   - `-425-625`  strong / saturated. Solid status backgrounds, and
  #                 also the canonical text-default-* color (DSFR
  #                 aliases text-default-success → success-425-625, etc.)
  #   - `-975-75`   lightest / alert background tint
  #   - `-950-100`  lighter / low-emphasis status surfaces
  #   - `-925-125`  light / docs-only reference (NOT in `dsfr.css`)
  #   - `-850-200`  softest / docs-only reference (NOT in `dsfr.css`)
  # Only `-425-625`, `-950-100`, and `-975-75` are compiled into the
  # canonical CSS distribution; the other three are reference values
  # listed in the DSFR's palette page for design-time use.
  # All four families pass WCAG AA at body text size on their `-975-75`
  # alert background using their `-425-625` for text.
  info-main-525:                  "#0078f3"
  info-425-625:                   "#0063cb"
  info-425-625-hover:             "#3b87ff"
  info-425-625-active:            "#6798ff"
  info-975-75:                    "#f4f6ff"
  info-950-100:                   "#e8edff"
  info-950-100-hover:             "#c2d1ff"
  info-950-100-active:            "#a9bfff"
  info-925-125:                   "#dde5ff"
  info-850-200:                   "#bccdff"
  warning-main-525:               "#d64d00"
  warning-425-625:                "#b34000"
  warning-425-625-hover:          "#ff6218"
  warning-425-625-active:         "#ff7a55"
  warning-975-75:                 "#fff4f3"
  warning-950-100:                "#ffe9e6"
  warning-950-100-hover:          "#ffc6bd"
  warning-950-100-active:         "#ffb0a2"
  warning-925-125:                "#ffded9"
  warning-850-200:                "#ffbeb4"
  error-main-525:                 "#f60700"
  error-425-625:                  "#ce0500"
  error-425-625-hover:            "#ff2725"
  error-425-625-active:           "#ff4140"
  error-975-75:                   "#fff4f4"
  error-950-100:                  "#ffe9e9"
  error-950-100-hover:            "#ffc5c5"
  error-950-100-active:           "#ffafaf"
  error-925-125:                  "#ffdddd"
  error-850-200:                  "#ffbdbd"
  success-main-525:               "#1f8d49"
  success-425-625:                "#18753c"
  success-425-625-hover:          "#27a959"
  success-425-625-active:         "#2fc368"
  success-975-75:                 "#dffee6"
  success-950-100:                "#b8fec9"
  success-950-100-hover:          "#46fd89"
  success-950-100-active:         "#34eb7b"
  success-925-125:                "#88fdaa"
  success-850-200:                "#3bea7e"

  # ---------- Illustrative accents (12 families, accent-only) ----------
  # Intentionally orphaned at the YAML level — these are NOT referenced by any
  # component. The linter will flag them as `orphaned-tokens`; this is desired.
  green-tilleul-verveine-main-707:  "#b7a73f"
  green-bourgeon-main-640:          "#68a532"
  green-emeraude-main-632:          "#00a95f"
  green-menthe-main-548:            "#009081"
  green-archipel-main-557:          "#009099"
  blue-ecume-main-400:              "#465f9d"
  blue-cumulus-main-526:            "#417dc4"
  purple-glycine-main-494:          "#a558a0"
  pink-macaron-main-689:            "#e18b76"
  pink-tuile-main-556:              "#ce614a"
  yellow-tournesol-main-731:        "#c8aa39"
  yellow-moutarde-main-679:         "#c3992a"
  orange-terre-battue-main-645:     "#e4794a"
  brown-cafe-creme-main-782:        "#d1b781"
  brown-caramel-main-648:           "#c08c65"
  brown-opera-main-680:             "#bd987a"
  beige-gris-galet-main-702:        "#aea397"

  # ============================================================
  # DECISION TOKENS — what components MUST reference
  # ============================================================
  # These abstract over light vs dark theme. The values below resolve to
  # the LIGHT theme. The dark-theme equivalents are documented in prose
  # (see "## Colors → Decision tokens").

  primary:                         "{colors.blue-france-sun-113-625}"
  on-primary:                      "{colors.grey-1000-50}"
  primary-hover:                   "{colors.blue-france-sun-113-625-hover}"
  primary-active:                  "{colors.blue-france-sun-113-625-active}"
  secondary:                       "{colors.red-marianne-main-472}"
  on-secondary:                    "{colors.grey-1000-50}"

  background-default:              "{colors.grey-1000-50}"
  background-alt:                  "{colors.grey-975-100}"
  background-contrast-grey:        "{colors.grey-950-150}"
  background-action-low-blue-france: "{colors.blue-france-925-125}"

  text-default-grey:               "{colors.grey-50-1000}"
  text-mention-grey:               "{colors.grey-425-625}"
  text-title-blue-france:          "{colors.blue-france-sun-113-625}"
  text-action-high-blue-france:    "{colors.blue-france-sun-113-625}"
  text-inverted-blue-france:       "{colors.grey-1000-50}"

  border-default-grey:             "{colors.grey-900-175}"
  border-action-high-blue-france:  "{colors.blue-france-sun-113-625}"
  border-plain-success:            "{colors.success-425-625}"
  border-plain-warning:            "{colors.warning-425-625}"
  border-plain-error:              "{colors.error-425-625}"
  border-plain-info:               "{colors.info-425-625}"

  focus-ring:                      "#0a76f6"

  success:                         "{colors.success-425-625}"
  warning:                         "{colors.warning-425-625}"
  error:                           "{colors.error-425-625}"
  info:                            "{colors.info-425-625}"

typography:
  # Marianne — sans-serif, the primary government typeface.
  display-xl:
    fontFamily: Marianne
    fontSize: 2.5rem        # 40px
    fontWeight: 700
    lineHeight: 3rem        # 48px
  h1:
    fontFamily: Marianne
    fontSize: 2.5rem
    fontWeight: 700
    lineHeight: 3rem
  h2:
    fontFamily: Marianne
    fontSize: 2rem          # 32px
    fontWeight: 700
    lineHeight: 2.5rem
  h3:
    fontFamily: Marianne
    fontSize: 1.75rem       # 28px
    fontWeight: 700
    lineHeight: 2.25rem
  h4:
    fontFamily: Marianne
    fontSize: 1.5rem        # 24px
    fontWeight: 700
    lineHeight: 2rem
  h5:
    fontFamily: Marianne
    fontSize: 1.25rem       # 20px
    fontWeight: 700
    lineHeight: 1.75rem
  h6:
    fontFamily: Marianne
    fontSize: 1.125rem      # 18px
    fontWeight: 700
    lineHeight: 1.5rem
  body-lg:
    fontFamily: Marianne
    fontSize: 1.125rem      # 18px
    fontWeight: 400
    lineHeight: 1.75rem
  body-md:
    fontFamily: Marianne
    fontSize: 1rem          # 16px
    fontWeight: 400
    lineHeight: 1.5rem
  body-sm:
    fontFamily: Marianne
    fontSize: 0.875rem      # 14px
    fontWeight: 400
    lineHeight: 1.5rem
  body-xs:
    fontFamily: Marianne
    fontSize: 0.75rem       # 12px
    fontWeight: 400
    lineHeight: 1.25rem
  label:
    fontFamily: Marianne
    fontSize: 0.875rem
    fontWeight: 700
    lineHeight: 1.5rem
  # Spectral — serif, secondary; reserved for distinguishing minor/secondary text.
  body-md-alt:
    fontFamily: Spectral
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.5rem
  body-sm-alt:
    fontFamily: Spectral
    fontSize: 0.875rem
    fontWeight: 400
    lineHeight: 1.5rem

rounded:
  none: 0px
  sm:   0.25rem    # used sparingly (search input top corners)
  md:   0.5rem
  pill: 9999px     # tags / badges

spacing:
  # Built on the DSFR `v` base unit: 1v = 0.25rem = 4px.
  # The Figma spec also references "W" units; W = 2v = 8px in this scale.
  0v:    0px
  0-5v:  0.125rem  # 2px
  1v:    0.25rem   # 4px
  1-5v:  0.375rem  # 6px
  2v:    0.5rem    # 8px  (1W)
  3v:    0.75rem   # 12px
  4v:    1rem      # 16px (2W) — standard inter-component gap
  5v:    1.25rem   # 20px
  6v:    1.5rem    # 24px (3W) — typical card padding
  7v:    1.75rem
  8v:    2rem      # 32px (4W) — section spacing
  10v:   2.5rem
  12v:   3rem      # 48px
  16v:   4rem      # 64px
  32v:   8rem      # 128px

components:
  # ============================================================
  # ACTIONS — Buttons (fr-btn, fr-btn--secondary, fr-btn--tertiary)
  # ============================================================
  button-primary:
    backgroundColor: "{colors.text-action-high-blue-france}"
    textColor:       "{colors.on-primary}"
    typography:      "{typography.body-md}"
    rounded:         "{rounded.none}"
    padding:         16px
    height:          40px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor:       "{colors.on-primary}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor:       "{colors.on-primary}"
  button-primary-disabled:
    backgroundColor: "{colors.background-contrast-grey}"
    textColor:       "{colors.text-mention-grey}"

  button-secondary:
    backgroundColor: "{colors.background-default}"
    textColor:       "{colors.text-action-high-blue-france}"
    typography:      "{typography.body-md}"
    rounded:         "{rounded.none}"
    padding:         16px
    height:          40px
  button-secondary-hover:
    backgroundColor: "{colors.blue-france-950-100-hover}"
    textColor:       "{colors.text-action-high-blue-france}"
  button-secondary-active:
    backgroundColor: "{colors.blue-france-950-100-active}"
    textColor:       "{colors.text-action-high-blue-france}"

  button-tertiary:
    backgroundColor: "transparent"
    textColor:       "{colors.text-action-high-blue-france}"
    typography:      "{typography.body-md}"
    rounded:         "{rounded.none}"
    padding:         16px
    height:          40px
  button-tertiary-hover:
    backgroundColor: "{colors.background-alt}"
    textColor:       "{colors.text-action-high-blue-france}"

  # ============================================================
  # FORMS — input, select, checkbox, radio, toggle
  # ============================================================
  input:
    backgroundColor: "{colors.background-contrast-grey}"
    textColor:       "{colors.text-default-grey}"
    typography:      "{typography.body-md}"
    rounded:         "{rounded.sm}"
    padding:         12px
    height:          40px
  input-focus:
    backgroundColor: "{colors.background-contrast-grey}"
    textColor:       "{colors.text-default-grey}"
  input-error:
    backgroundColor: "{colors.background-contrast-grey}"
    textColor:       "{colors.text-default-grey}"
  input-disabled:
    backgroundColor: "{colors.background-contrast-grey}"
    textColor:       "{colors.text-mention-grey}"

  select:
    backgroundColor: "{colors.background-contrast-grey}"
    textColor:       "{colors.text-default-grey}"
    typography:      "{typography.body-md}"
    rounded:         "{rounded.sm}"
    padding:         12px
    height:          40px

  checkbox:
    backgroundColor: "{colors.background-default}"
    textColor:       "{colors.text-default-grey}"
    rounded:         "{rounded.none}"
    size:            16px
  checkbox-checked:
    backgroundColor: "{colors.text-action-high-blue-france}"
    textColor:       "{colors.on-primary}"

  radio:
    backgroundColor: "{colors.background-default}"
    textColor:       "{colors.text-default-grey}"
    rounded:         "{rounded.pill}"
    size:            16px
  radio-checked:
    backgroundColor: "{colors.text-action-high-blue-france}"
    textColor:       "{colors.on-primary}"

  toggle:
    backgroundColor: "{colors.background-contrast-grey}"
    textColor:       "{colors.text-default-grey}"
    rounded:         "{rounded.pill}"
    width:           40px
    height:          24px
  toggle-on:
    backgroundColor: "{colors.text-action-high-blue-france}"
    textColor:       "{colors.on-primary}"

  # ============================================================
  # SURFACES — card, tile
  # ============================================================
  card:
    backgroundColor: "{colors.background-default}"
    textColor:       "{colors.text-default-grey}"
    typography:      "{typography.body-md}"
    rounded:         "{rounded.none}"
    padding:         24px
  card-hover:
    backgroundColor: "{colors.background-alt}"
    textColor:       "{colors.text-default-grey}"

  tile:
    backgroundColor: "{colors.background-default}"
    textColor:       "{colors.text-action-high-blue-france}"
    typography:      "{typography.body-md}"
    rounded:         "{rounded.none}"
    padding:         16px
  tile-hover:
    backgroundColor: "{colors.background-alt}"
    textColor:       "{colors.text-action-high-blue-france}"

  # ============================================================
  # TAGS & BADGES
  # ============================================================
  tag:
    backgroundColor: "{colors.background-action-low-blue-france}"
    textColor:       "{colors.text-action-high-blue-france}"
    typography:      "{typography.body-sm}"
    rounded:         "{rounded.pill}"
    padding:         12px
    height:          24px
  tag-sm:
    backgroundColor: "{colors.background-action-low-blue-france}"
    textColor:       "{colors.text-action-high-blue-france}"
    typography:      "{typography.body-xs}"
    rounded:         "{rounded.pill}"
    padding:         8px
    height:          20px

  badge:
    backgroundColor: "{colors.background-action-low-blue-france}"
    textColor:       "{colors.text-action-high-blue-france}"
    typography:      "{typography.body-sm}"
    rounded:         "{rounded.pill}"
    padding:         8px
    height:          24px
  badge-success:
    backgroundColor: "{colors.success-975-75}"
    textColor:       "{colors.success-425-625}"
  badge-warning:
    backgroundColor: "{colors.warning-975-75}"
    textColor:       "{colors.warning}"
  badge-error:
    backgroundColor: "{colors.error-975-75}"
    textColor:       "{colors.error}"
  badge-info:
    backgroundColor: "{colors.info-975-75}"
    textColor:       "{colors.info}"

  # ============================================================
  # FEEDBACK — alerts
  # ============================================================
  alert-success:
    backgroundColor: "{colors.success-975-75}"
    textColor:       "{colors.text-default-grey}"
    typography:      "{typography.body-md}"
    rounded:         "{rounded.none}"
    padding:         16px
  alert-warning:
    backgroundColor: "{colors.warning-975-75}"
    textColor:       "{colors.text-default-grey}"
    typography:      "{typography.body-md}"
    rounded:         "{rounded.none}"
    padding:         16px
  alert-error:
    backgroundColor: "{colors.error-975-75}"
    textColor:       "{colors.text-default-grey}"
    typography:      "{typography.body-md}"
    rounded:         "{rounded.none}"
    padding:         16px
  alert-info:
    backgroundColor: "{colors.info-975-75}"
    textColor:       "{colors.text-default-grey}"
    typography:      "{typography.body-md}"
    rounded:         "{rounded.none}"
    padding:         16px

  # ============================================================
  # NAVIGATION — breadcrumb, modal, callout, header, footer
  # ============================================================
  breadcrumb:
    backgroundColor: "{colors.background-default}"
    textColor:       "{colors.text-mention-grey}"
    typography:      "{typography.body-sm}"
    rounded:         "{rounded.none}"
    padding:         16px

  modal:
    backgroundColor: "{colors.background-default}"
    textColor:       "{colors.text-default-grey}"
    typography:      "{typography.body-md}"
    rounded:         "{rounded.none}"
    padding:         32px

  callout:
    backgroundColor: "{colors.background-alt}"
    textColor:       "{colors.text-default-grey}"
    typography:      "{typography.body-md}"
    rounded:         "{rounded.none}"
    padding:         24px

  header:
    backgroundColor: "{colors.background-default}"
    textColor:       "{colors.text-default-grey}"
    typography:      "{typography.body-md}"
    rounded:         "{rounded.none}"
    padding:         16px

  footer:
    backgroundColor: "{colors.background-default}"
    textColor:       "{colors.text-default-grey}"
    typography:      "{typography.body-sm}"
    rounded:         "{rounded.none}"
    padding:         32px
---

## Overview

The **Système de Design de l'État** (DSFR) is the official design system of the French Republic — the visual identity, component library, and accessibility framework that every `.gouv.fr` digital service is required to follow under [circulaire n°6411-SG](https://www.systeme-de-design.gouv.fr/version-courante/fr/a-propos/articles-et-actualites/circulaire-d-application-du-7-juillet-2023). It exists to *unify* State websites, to *improve the citizen experience*, and to *guarantee accessibility*.

Visually, the DSFR is **architectural and journalistic**: square corners by default, generous whitespace without ornament, a workhorse sans-serif (Marianne) doing 90% of the typographic load, and a single saturated brand colour — *Bleu France* `#000091` — used as a deliberate signal of officiality and primary action. Decoration is restrained; the State does not fashion-shop. Type and information hierarchy carry the design.

> **Accessibility baseline.** All components target the **RGAA** (*Référentiel Général d'Amélioration de l'Accessibilité*) — France's legal accessibility standard, broadly aligned with **WCAG 2.1 AA**. Concretely:
>
> - Body text contrast ≥ **4.5:1**; large text and UI components ≥ **3:1**.
> - **Visible focus** indicator on every interactive element (the DSFR uses a 2px outer halo in `focus-ring` `#0a76f6`).
> - Touch targets **≥ 44×44 px**.
> - Colour is never the sole carrier of information.

> **Theming.** The DSFR supports a light theme and a dark theme, switched via the `data-fr-scheme` attribute on `<html>` (`"system" | "light" | "dark"`). This `DESIGN.md` encodes the **light theme** in the YAML token graph. See [Colors → Decision tokens](#decision-tokens) below for the dark-theme mappings.

> **Brand & legal scope.** The Marianne wordmark, the *République Française* logo, and the use of *Bleu France* as a State mark are reserved by law for official .gouv.fr services. This file is a derived, machine-readable description; for production .gouv.fr builds always use the canonical [`@gouvfr/dsfr`](https://www.npmjs.com/package/@gouvfr/dsfr) npm package.

## Colors

The DSFR palette is rooted in the French State's graphic charter. Every colour is a **design token** — a transverse name shared across Sketch, Figma, SCSS variables and CSS custom properties. Tokens come in two flavours: **option tokens** (raw palette values) and **decision tokens** (the names UI code references). A well-implemented DSFR site never references option tokens directly.

### Marque de l'État (brand colours)

The brand is built on two anchors — **Bleu France** and **Rouge Marianne** — with white absorbed into the neutrals.

- **Bleu France** `#000091` — the State's primary signal. Reserved for **primary actions** (CTA buttons), **active states**, and **brand surfaces** (the *bloc marque*). Hover `#1212ff`, active `#2323ff`. Light variants step down through `#cacafb` → `#e3e3fd` → `#ececfe` → `#f5f5fe` for low-contrast surfaces (selected list rows, badges, action backgrounds).
- **Rouge Marianne** `#e1000f` — used **sparingly**, attached to the Marianne identity (logo lockups, emphasis in editorial contexts). Hover `#f93f42`, active `#f95a5c`. *Not* a generic destructive-action red — that role belongs to `error` (`#ce0500`).

### Neutrals

A 10-step grey scale handles backgrounds, text, borders, and dividers:

| Role | Light theme | Token |
|------|-------------|-------|
| Page background | `#ffffff` | `grey-1000-50` |
| Alt background | `#f6f6f6` | `grey-975-100` |
| Contrast surface (inputs) | `#eeeeee` | `grey-950-150` |
| Default border | `#dddddd` | `grey-900-175` |
| Mention / placeholder text | `#666666` | `grey-425-625` |
| Body text | `#161616` | `grey-50-1000` |

### System (functional) colours

Reserved for **system feedback only** — never decorative.

| Role | Hex (`-425-625`) | Tinted background (`-950-100`) | Alert background (`-975-75`) |
|------|------------------|-------------------------------|------------------------------|
| Success | `#18753c` | `#b8fec9` | `#dffee6` |
| Warning | `#b34000` | `#ffe9e6` | `#fff4f3` |
| Error   | `#ce0500` | `#ffe9e9` | `#fff4f4` |
| Info    | `#0063cb` | `#e8edff` | `#f4f6ff` |

Each interactive shade (`-425-625` and `-950-100`) ships explicit `-hover` and `-active` states; `-975-75` does not (alerts are not actionable surfaces).

### Illustrative accents

The DSFR ships **12 illustrative families** for complementary editorial use — *tilleul-verveine*, *bourgeon*, *émeraude*, *menthe*, *archipel*, *écume*, *cumulus*, *glycine*, *macaron*, *tuile*, *tournesol*, *moutarde*, *terre-battue*, *café-crème*, *caramel*, *opéra*, *gris-galet*. Rules:

1. **One family per page**, never combined.
2. **Never** for actions or system states (those use Bleu France and the system colours, respectively).
3. Used to add hierarchy, theme a section, or distinguish content categories.

(In the YAML graph these tokens are intentionally **orphaned** — the linter will emit `orphaned-tokens` warnings, which is correct.)

### Decision tokens

UI code must reference these, not the option layer. The table below lists the mapping for both themes — the YAML encodes the light column; the dark column is the value an implementation should resolve when `data-fr-scheme="dark"` is active.

| Decision token | Light | Dark |
|----------------|-------|------|
| `primary` / `text-action-high-blue-france` | `#000091` (sun-113) | `#8585f6` (625) |
| `primary-hover` | `#1212ff` | `#9d9dff` |
| `primary-active` | `#2323ff` | `#b1b1ff` |
| `background-default` | `#ffffff` (grey-1000) | `#1e1e1e` (grey-50) |
| `background-alt` | `#f6f6f6` (grey-975) | `#2a2a2a` (grey-100) |
| `background-contrast-grey` | `#eeeeee` (grey-950) | `#353535` (grey-150) |
| `background-action-low-blue-france` | `#e3e3fd` (925) | `#21213f` (125) |
| `text-default-grey` | `#161616` | `#cecece` |
| `text-mention-grey` | `#666666` | `#929292` |
| `border-default-grey` | `#dddddd` | `#353535` |
| `focus-ring` | `#0a76f6` | `#0a76f6` |

> **Critical rule.** Don't apply Bleu France to non-interactive titles. The DSFR reserves it for *clickable* elements; using it on a heading creates ambiguity with links and buttons.

## Typography

### Faces

- **Marianne** (primary, sans-serif). The State's bespoke typeface. Use weights `light` (300), `regular` (400), `bold` (700), each with italics. **Fallback**: Arial.
- **Spectral** (secondary, serif). Weights `regular` (400) and `extra-bold` (800). Reserved for *secondary, minor, or distinguishing* text — applied via the `fr-text--alt` class. **Fallback**: Georgia.

> The DSFR explicitly recommends *not* using Spectral as the primary face. It's an accent.

### Scale

| Token | Size | Weight | Use |
|-------|------|--------|-----|
| `display-xl` / `h1` | 2.5rem (40px) | 700 | Hero / page title |
| `h2` | 2rem (32px) | 700 | Major section |
| `h3` | 1.75rem (28px) | 700 | Subsection |
| `h4` | 1.5rem (24px) | 700 | Block heading |
| `h5` | 1.25rem (20px) | 700 | Inline heading |
| `h6` | 1.125rem (18px) | 700 | Smallest heading |
| `body-lg` | 1.125rem (18px) | 400 | Lead paragraph |
| `body-md` | 1rem (16px) | 400 | Default body |
| `body-sm` | 0.875rem (14px) | 400 | Metadata, secondary |
| `body-xs` | 0.75rem (12px) | 400 | Captions, microcopy |
| `label` | 0.875rem (14px) | 700 | Form labels, button text |

Mobile renders one step down on `display-xl`/`h1`/`h2` (handled by `@media` rules in DSFR's CSS — agents emitting markup should rely on the `fr-h1`…`fr-h6` classes which carry the responsive logic).

### Rules

- Body line-height: `1.5rem` (1.5× on `body-md`) for comfortable long-form reading.
- Use sentence case for headings; reserve uppercase for utility microcopy with expanded letter-spacing (e.g. `fr-link--icon` labels).
- **Never** colour a title in Bleu France (see Colors).
- For all-caps utility microcopy, set letter-spacing `0.06em`.

## Layout

### Container & grid

- **Max content width**: `78rem` (1248 px). Wider hero / footer surfaces extend full-bleed but content wraps to this max.
- **Grid**: 12 columns. Gutters: 16px mobile / 24px tablet / 32px desktop.
- **Side padding**: 24px mobile / 40px desktop.

### Breakpoints

| Name | Range |
|------|-------|
| `xs` | < 576 px |
| `sm` | ≥ 576 px |
| `md` | ≥ 768 px |
| `lg` | ≥ 992 px |
| `xl` | ≥ 1200 px |

The DSFR class system uses suffixed modifiers (`fr-grid-row--gutters`, `fr-col-md-6`) keyed on the breakpoints above.

### Spacing system

The DSFR is built on the **`v` unit**: `1v = 0.25rem = 4px`. The Figma library and the `fr-mb-Xv` / `fr-py-Xv` utility classes both reference this scale.

| Token | Value | Common use |
|-------|-------|------------|
| `1v`  | 4px   | Hairline spacing |
| `2v` (`1W`) | 8px | Tight inline gaps |
| `3v`  | 12px | Compact stack |
| `4v` (`2W`) | 16px | **Default inter-component gap** (button group, form rows) |
| `6v` (`3W`) | 24px | Card / container padding |
| `8v` (`4W`) | 32px | Section spacing |
| `12v` | 48px | Large section gap |
| `16v` | 64px | Hero / page-level rhythm |

> **Whitespace philosophy.** Generous but utilitarian — *espace pour respirer*, not *espace pour épater*. The State is sober; the layout reflects that.

## Elevation & Depth

The DSFR is **flat by default**. Shadows are reserved for ephemeral surfaces and meaningful state changes:

| Token | Shadow | Use |
|-------|--------|-----|
| `e-0` | none | Default for cards, tiles, panels |
| `e-1` | `0 1px 2px rgba(0, 0, 18, 0.16)` | Subtle separation (rarely used) |
| `e-2` | `0 4px 8px rgba(0, 0, 18, 0.16)` | Modals, dialogs |
| `e-3` | `0 8px 16px rgba(0, 0, 18, 0.16)` | Dropdowns, popovers, on-hover lift for cards |

> **Focus ≠ shadow.** Visible focus is rendered as a **2px outer halo** in `focus-ring` (`#0a76f6`), drawn with `outline` rather than `box-shadow`. This is a hard accessibility requirement — never replace it with a shadow.

## Shapes

Corners are **square by convention**. `rounded.none = 0` is the default for almost every component: buttons, cards, modals, alerts, inputs (mostly), tiles, panels.

Documented exceptions:

| Component | Radius | Token |
|-----------|--------|-------|
| Search input (top corners) | 4px | `rounded.sm` |
| Tags, badges, pills | full | `rounded.pill` |
| Toggle switch knob/track | full | `rounded.pill` |

> **Rationale.** Angularity reinforces officiality, restraint, and republican neutrality. Rounded corners would soften the visual register away from the State register the DSFR is designed to preserve.

## Components

Each component below is described once, then surfaced in the YAML token graph as `<component-name>` plus `<component-name>-<state>` entries. State variants follow the alpha `DESIGN.md` convention of separate component entries.

For each component, the **BEM class** column gives the canonical `fr-*` name an implementing agent should emit when generating real HTML — these classes pick up the JS behaviour shipped in `dsfr.module.min.js` automatically.

### Actions

| Component | BEM class | Notes |
|-----------|-----------|-------|
| Primary button | `.fr-btn` | Bleu France background, white text, no radius, 40 px height (`md`). Sizes: `--sm` (32 px), default `md`, `--lg` (48 px). |
| Secondary button | `.fr-btn.fr-btn--secondary` | White background, Bleu France text + 1px border. |
| Tertiary button | `.fr-btn.fr-btn--tertiary` (`--no-outline` for borderless) | Transparent background, Bleu France text. |

Group buttons with `.fr-btns-group` (default vertical with 2W gap; `--inline` for horizontal at a breakpoint; `--equisized` to match widths).

### Forms

| Component | BEM class |
|-----------|-----------|
| Input | `.fr-input` (wrap in `.fr-input-group`; add `.fr-input-group--error` / `--valid` for state) |
| Select | `.fr-select` |
| Checkbox | `.fr-checkbox-group` + native `<input type="checkbox">` |
| Radio | `.fr-radio-group` + native `<input type="radio">` |
| Toggle (interrupteur) | `.fr-toggle` |

Form rules: every input has a visible `<label>`; error messages use `.fr-error-text` with the `error` colour and a 16 px top margin from the input.

### Surfaces

| Component | BEM class |
|-----------|-----------|
| Card (carte) | `.fr-card` (`--horizontal` for side-by-side image; `--no-arrow` to hide the action chevron) |
| Tile (tuile) | `.fr-tile` (smaller, denser variant of card; primary content is a single link) |
| Callout (mise en avant) | `.fr-callout` |

Cards are flat at rest; on `:hover` they may apply `e-3` to suggest interactivity if the entire card is a link.

### Tags & badges

| Component | BEM class |
|-----------|-----------|
| Tag | `.fr-tag` (sizes `--sm`, default; can be `<a>` or `<button>` for selectable) |
| Badge | `.fr-badge` (variants `--success`, `--warning`, `--error`, `--info`, `--new`) |

Tags and badges are the **only** components that use `rounded.pill`.

### Feedback

| Component | BEM class |
|-----------|-----------|
| Alert | `.fr-alert` + `.fr-alert--success | --warning | --error | --info`; size suffixes `--sm` |
| Notice (bandeau d'information) | `.fr-notice` |

Alerts include a leading icon (info/check/exclamation/cross) and an optional close button (`.fr-btn--close`).

### Navigation & branding

| Component | BEM class |
|-----------|-----------|
| Breadcrumb (fil d'Ariane) | `.fr-breadcrumb` |
| Modal (modale) | `.fr-modal` (focus trap + scroll lock provided by the JS) |
| Header (en-tête) | `.fr-header` (includes `.fr-header__brand`, `.fr-header__service`, `.fr-header__tools`) |
| Footer (pied de page) | `.fr-footer` (includes `.fr-footer__brand`, `.fr-footer__bottom`, `.fr-footer__partners`) |

The header is the brand carrier: the Marianne lockup (*"République Française"*) sits in `.fr-header__brand`, and the operator/service lockup sits beside it in `.fr-header__service`. This is the canonical *bloc marque* and must be present on every State page.

## Do's and Don'ts

### ✅ Do

- Reference **decision tokens** (`text-action-high-blue-france`, `background-default`, `border-default-grey`) in components — never option tokens directly.
- Pair every interactive element with a **visible focus state** drawn with `focus-ring` as an outline.
- Use **`data-fr-scheme`** for theme switching; never hard-code colours per theme.
- Keep **touch targets ≥ 44×44 px** (button `--sm` is 32 px tall but its hit-area is padded to compensate).
- Choose **one illustrative family per page** when accenting editorial content.
- Use Marianne as the workhorse face; reserve Spectral (`fr-text--alt`) for secondary or distinguishing text.
- Lint the `DESIGN.md` against the Stitch CLI before publishing changes (`npx @google/design.md lint DESIGN.md`).

### ❌ Don't

- **Don't** apply Bleu France to titles or to any non-interactive text — it's reserved for actions.
- **Don't** introduce border-radius on buttons, cards, modals, alerts. Square corners are intentional.
- **Don't** mix light-theme and dark-theme tokens in the same context.
- **Don't** use the Marianne logo, the *République Française* lockup, or Bleu France as a brand mark outside an authorised .gouv.fr context.
- **Don't** add resting-state shadows to plain cards — reserve elevation for menus, modals, and hover lift.
- **Don't** use the illustrative palette for actions or system states.
- **Don't** treat Rouge Marianne as a destructive-action red — use the `error` token (`#ce0500`).
- **Don't** colour a heading with `primary` even if it looks attractive — accessibility audits and DSFR conformance both flag it.

---

> **References used to build this file.**
> DSFR documentation — <https://www.systeme-de-design.gouv.fr> ·
> DSFR source — <https://github.com/GouvernementFR/dsfr> ·
> `DESIGN.md` spec — <https://github.com/google-labs-code/design.md>.
