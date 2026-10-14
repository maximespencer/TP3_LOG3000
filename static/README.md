# `static/` — Ressources statiques du frontend

## Raison d'être

Contient les fichiers servis tels quels par Flask (sans passer par le moteur de
gabarits). Flask expose automatiquement ce dossier sous l'URL `/static/`.

## Fichiers

| Fichier | Responsabilité |
|---|---|
| `style.css` | Mise en forme de la calculatrice : centrage de la page, thème sombre, écran (`#display`), grille 4×4 du clavier (`.buttons`), boutons (`.btn`) et touches d'opération mises en évidence (`.operator`). |

## Dépendances et hypothèses

- Chargé par `templates/index.html` via `url_for('static', filename='style.css')`.
- Les sélecteurs CSS supposent la structure HTML du gabarit (`.calculator`,
  `#display`, `.buttons`, `.btn`, `.operator`) : renommer une classe dans le HTML
  exige de la renommer ici aussi.
- Aucune dépendance externe (pas de framework CSS, pas de police distante).
