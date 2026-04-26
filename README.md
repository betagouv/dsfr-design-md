# DSFR · `DESIGN.md`

Encodage du **Système de Design de l'État Français** (DSFR) au format `DESIGN.md`, à destination des agents de codage IA.

Ce dépôt publie un fichier `DESIGN.md` faisant office de source unique de vérité, qui traduit le système de design officiel de l'État français — couleurs, typographie, espacements et patrons de composants — vers le **format ouvert `DESIGN.md`** spécifié par Google Stitch ([`google-labs-code/design.md`](https://github.com/google-labs-code/design.md)).

L'objectif est simple : **permettre à n'importe quel agent de codage compatible DESIGN.md (Stitch, Claude Code, Cursor, Kiro, Windsurf, Letta Code, …) de générer par défaut des interfaces qui ressemblent et se comportent comme un site `.gouv.fr`.**

---

## Pourquoi ce projet existe

Le DSFR est le [système de design obligatoire](https://www.systeme-de-design.gouv.fr/version-courante/fr/a-propos/articles-et-actualites/circulaire-d-application-du-7-juillet-2023) pour les services web de l'État (circulaire n°6411-SG). Il est distribué sous le nom `@gouvfr/dsfr` sur npm — une boîte à outils HTML/CSS/JS complète comportant plus de 50 composants accessibles — mais les agents de codage qui génèrent des interfaces à partir d'un prompt en langage naturel ne lisent pas les fichiers SCSS.

Le format `DESIGN.md` de Stitch a été conçu spécifiquement pour combler cet écart : un document hybride YAML front matter + Markdown qui donne aux agents une **compréhension persistante et structurée d'un système de design**, validable contre les critères WCAG via `npx @google/design.md lint`.

Ce projet fait le pont entre les deux.

---

## Contenu du dépôt

```
.
├── DESIGN.md          ← le système de design, au format DESIGN.md
├── preview.html       ← catalogue visuel — thème clair
├── preview-dark.html  ← catalogue visuel — thème sombre
├── README.md          ← ce fichier
└── .gitignore
```

Les fichiers `preview.html` et `preview-dark.html` sont des pages HTML autonomes (sans script, sans étape de build) qui rendent l'ensemble des tokens et composants documentés dans `DESIGN.md`. Elles servent de **test de cohérence visuelle** : si une valeur manque ou diverge dans le YAML, le composant correspondant casse à l'écran. Marianne et Spectral sont chargées depuis le CDN officiel `@gouvfr/dsfr` pour la fidélité typographique.

Le `DESIGN.md` couvre :

| Couche | Contenu |
|--------|---------|
| **YAML front matter** | Tokens d'option Bleu France et Rouge Marianne, neutres, couleurs système (succès/avertissement/erreur/information), accents illustratifs (12 familles), tokens de décision, échelle typographique Marianne et Spectral, échelle d'espacement basée sur le `v`, échelle de rayons de bord, environ 15 composants centraux (boutons, champs de saisie, listes déroulantes, cases à cocher, boutons radio, interrupteurs, cartes, tuiles, tags, alertes, badges, modales, fils d'Ariane, mises en avant, en-têtes/pieds de page) avec leurs variantes d'état hover/active/focus/disabled. |
| **Corps Markdown** | 8 sections canoniques — Aperçu · Couleurs · Typographie · Mise en page · Élévation et profondeur · Formes · Composants · À faire et à ne pas faire — qui expliquent le *pourquoi* derrière chaque valeur, y compris les règles propres au DSFR comme « ne jamais appliquer le Bleu France à un titre » et le mécanisme `data-fr-scheme` pour le basculement clair/sombre. |

Le fichier cible le **thème clair**. La correspondance des tokens de décision pour le thème sombre est documentée en prose, parce que la spécification `DESIGN.md` en version alpha ne dispose pas encore d'un mécanisme de bascule de thème natif.

---

## Utilisation

### Importer dans Google Stitch

1. Ouvrez votre projet Stitch.
2. **Settings → Design System → Import DESIGN.md**.
3. Collez le contenu du fichier (ou téléversez-le).
4. Générez vos prompts comme à l'accoutumée : Stitch appliquera automatiquement les couleurs DSFR, la typographie, les coins carrés et les patrons de composants.

### Utiliser avec d'autres agents de codage

Déposez `DESIGN.md` à la racine de votre projet. La plupart des agents modernes (Claude Code, Cursor, Kiro, Windsurf, Letta Code) le récupéreront comme contexte de design. Certains agents acceptent un drapeau `--design-md` ; consultez leur documentation.

### Linter et valider

```bash
npx @google/design.md lint DESIGN.md
```

Cette commande vérifie les références de tokens cassées, l'absence de couleur primaire, les violations de contraste vis-à-vis du WCAG AA (4.5:1), les tokens orphelins et l'ordre des sections.

**Sortie attendue du linter** : `0 erreur, ≈41 avertissements, 1 info` — chaque avertissement est un cas `orphaned-tokens` et est intentionnel :

- Les 16 couleurs de la **palette illustrative** (tilleul-verveine, glycine, tournesol, etc.) sont des accents par règle DSFR ; elles ne doivent pas être référencées par les boutons ou les composants système.
- Les **tokens d'option** bruts (par exemple `blue-france-main-525`, `red-marianne-*`) sont conservés comme couche de référence documentaire. Le code d'interface est censé consommer les **tokens de décision** qui pointent vers eux — ces derniers *sont* bien référencés par les composants.
- `focus-ring` et `border-default-grey` nécessiteraient des propriétés de composant (`outline`, `borderColor`) que la spécification `DESIGN.md` alpha ne définit pas encore.

Si la spécification gagne ces propriétés dans une version future, ce fichier devra être mis à jour pour brancher les orphelins.

### Exporter vers d'autres formats

```bash
# Thème Tailwind
npx @google/design.md export --format tailwind DESIGN.md > tailwind.theme.json

# tokens.json au format W3C DTCG
npx @google/design.md export --format dtcg     DESIGN.md > tokens.json
```

---

## Mises en garde importantes

### ⚠️ Cadre légal et identité de marque

L'identité visuelle du DSFR — le bloc-marque Marianne, le logotype *République Française*, la couleur Bleu France utilisée comme marque d'État, et la fonte Marianne — est **légalement réservée aux sites et applications officiels de l'État français**. Pour reprendre les conditions d'utilisation du DSFR :

> Il est formellement interdit à tout autre acteur d'utiliser le Système de Design de l'État (les administrations territoriales ou tout autre acteur privé) pour des sites web ou des applications.

Ce `DESIGN.md` est une **description dérivée et lisible par machine** du système de design, utile pour :

- ✅ Les équipes État (services `.gouv.fr`) qui construisent avec des agents IA.
- ✅ Des usages éducatifs et de recherche.
- ✅ Le prototypage d'outils internes qui finiront par utiliser le paquet canonique `@gouvfr/dsfr`.

Ce n'est **pas** une licence pour estampiller des services tiers comme étant gouvernementaux. Pour toute mise en production sur un service `.gouv.fr`, utilisez le paquet npm officiel `@gouvfr/dsfr`.

### ⚠️ La spécification est en alpha

Le format `DESIGN.md` de Stitch est actuellement en version `alpha`. Le schéma des tokens et le comportement de la CLI peuvent évoluer. Pensez à figer une version précise de `@google/design.md` dans toute chaîne d'intégration automatisée.

### ⚠️ Encodage avec perte

Le DSFR est plus riche que ce que la spécification alpha peut représenter — granularité des tokens d'option, tokens de décision, bascule double thème, palettes illustratives, règles d'accessibilité spécifiques au RGAA. Nous captons l'essentiel en YAML et documentons le reste en prose. Pour la fidélité canonique, référez-vous toujours à :

- **Source de vérité (visuelle)** : <https://www.systeme-de-design.gouv.fr/version-courante/fr>
- **Source de vérité (code)** : [`@gouvfr/dsfr`](https://www.npmjs.com/package/@gouvfr/dsfr) — `node_modules/@gouvfr/dsfr/dist/core/colors.json`

---

## Statut du projet

Ce dépôt est une **preuve de concept** réalisée par [@kaaloo](https://github.com/kaaloo) (beta.gouv.fr) afin d'évaluer l'utilité d'un `DESIGN.md` officiel pour le DSFR. Si l'expérience est concluante, l'objectif est de proposer aux mainteneurs `@GouvernementFR` la reprise du fichier dans le dépôt canonique [`GouvernementFR/dsfr`](https://github.com/GouvernementFR/dsfr) ou un dépôt voisin.

Retours, issues et pull requests bienvenus.

---

## Sources et références

- Documentation du DSFR — <https://www.systeme-de-design.gouv.fr>
- Dépôt du DSFR — <https://github.com/GouvernementFR/dsfr>
- Spécification `DESIGN.md` — <https://github.com/google-labs-code/design.md>
- Annonce Stitch — <https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-design-md/>
- W3C Design Tokens Format Module — <https://tr.designtokens.org/format/>

---

## Licence

Le contenu `DESIGN.md` de ce dépôt est publié sous **MIT** (en cohérence avec la licence du code source du DSFR), **avec la mise en garde explicite ci-dessus** concernant l'identité visuelle. La fonte Marianne **n'est pas** redistribuée ici — référez-vous au [LICENSE.md du DSFR](https://github.com/GouvernementFR/dsfr/blob/main/LICENSE.md) pour les conditions d'usage de la fonte.
