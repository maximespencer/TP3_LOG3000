# `templates/` — Gabarits HTML (Jinja2)

## Raison d'être

Contient l'interface utilisateur. Flask cherche les gabarits dans ce dossier
lorsque `render_template()` est appelé dans `app.py`.

## Fichiers

| Fichier | Responsabilité |
|---|---|
| `index.html` | Page unique de la calculatrice : écran en lecture seule, clavier de 16 boutons (chiffres 0-9, `+ - * /`, `C`, `=`) et deux fonctions JavaScript (`appendToDisplay`, `clearDisplay`). |

## Fonctionnement

1. Les boutons de chiffres et d'opérateurs ajoutent un caractère à l'écran côté
   client (JavaScript), sans requête au serveur.
2. `C` vide l'écran côté client.
3. `=` soumet le formulaire en `POST /` avec le champ `display` contenant
   l'expression.
4. `app.py` calcule le résultat et réaffiche la page avec la variable Jinja
   `{{ result }}` placée dans l'écran (résultat ou message `Error: ...`).

## Dépendances et hypothèses

- Rendu par Flask/Jinja2 ; la variable `result` doit être fournie par la vue.
- Utilise `static/style.css` pour le style.
- Le nom du champ `display` est un contrat avec `app.py`
  (`request.form.get('display')`) : ne pas le renommer d'un seul côté.
- JavaScript doit être activé dans le navigateur pour saisir une expression.
