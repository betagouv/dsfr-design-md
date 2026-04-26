# Feuille de route

Travail différé sur ce dépôt, par ordre de priorité. Les automatisations sont volontairement repoussées tant que la spécification (`DESIGN.md`) n'est pas stabilisée par rapport à la source canonique du DSFR (`@gouvfr/dsfr/dist/dsfr.css`).

## 1. Action GitHub de lint *(différée)*

Exécuter sur chaque PR&nbsp;:

```bash
npx @google/design.md@latest lint DESIGN.md
```

Bloque la fusion en cas d'erreur. Effort&nbsp;: faible. Valeur&nbsp;: immédiate.

## 2. Action de parité avec le DSFR *(différée — c'est l'enjeu structurant)*

Tâche planifiée qui&nbsp;:

1. Télécharge `@gouvfr/dsfr@latest/dist/dsfr.css`.
2. Extrait chaque déclaration `--couleur: #hex;` (clair + sombre).
3. La compare au YAML d'options du `DESIGN.md`.
4. Ouvre une *issue* en cas de divergence.

C'est la défense structurelle contre la classe de dérive que nous avons rencontrée pendant le développement initial (voir `## Historique` dans la mémoire interne du projet)&nbsp;: une option-token mal recopiée, une nuance manquante, une teinte mal étiquetée. Effort&nbsp;: moyen. Valeur&nbsp;: élevée à long terme.

## 3. Fichier compagnon `AGENTS.md`

Document parallèle au `DESIGN.md`, ciblé sur les agents IA consommateurs (et non sur les designers humains). Doit&nbsp;:

- Restater les restrictions légales sur l'usage du *Bleu France* et de *Marianne*.
- Documenter la convention « tokens orphelins » (volontairement non référencés par les composants).
- Pointer sur le `DESIGN.md` comme source de vérité pour les tokens et composants.

## 4. *Tag* `v0.1.0`

Une fois que la spécification est jugée stable et alignée à 100 % avec le DSFR canonique.

## 5. Discussion sur `@GouvernementFR/dsfr`

Ouvrir une *issue* ou une *discussion* proposant l'adoption du format `DESIGN.md` côté DSFR (pour publication officielle ou comme artefact dérivé).

---

> Pour les contributeurs&nbsp;: voir aussi `README.md` (présentation et caveats légaux) et `DESIGN.md` (la spécification elle-même).
