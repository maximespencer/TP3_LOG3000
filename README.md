# Calculatrice Flask — LOG3000 TP3

**Équipe :** 
**Membres :** 

## 1. But et portée du projet

Ce dépôt contient une calculatrice web minimaliste. L'interface (HTML/CSS/JS)
permet de composer une expression à l'aide d'un clavier à l'écran ; le serveur
Flask (Python) l'analyse et renvoie le résultat dans la même page.

**Fonctionnalités couvertes**

- Les quatre opérations de base : addition `+`, soustraction `-`,
  multiplication `*`, division réelle `/`.
- Une seule opération par expression, sous la forme `<nombre> <op> <nombre>`
  (ex. `12*3`, `7.5/2`, `-4+10`).
- Nombres décimaux et opérandes négatifs.
- Messages d'erreur affichés dans l'écran (`Error: ...`) pour les expressions
  invalides ou la division par zéro.

**Hors portée** : priorité des opérateurs, expressions à plusieurs opérations,
parenthèses, fonctions scientifiques, historique des calculs.

## 2. Structure du dépôt

```
.
├── app.py             # Serveur Flask : route "/" et analyse des expressions (calculate)
├── operators.py       # Fonctions arithmétiques add / subtract / multiply / divide
├── requirements.txt   # Dépendances Python (Flask, pytest)
├── templates/         # Gabarit HTML de l'interface        -> voir templates/README.md
├── static/            # Feuille de style CSS               -> voir static/README.md
└── tests/             # Suite de tests automatisés pytest  -> voir tests/README.md
```

Le backend se trouve à la racine : `app.py` reçoit l'expression, la découpe en
deux opérandes et un opérateur, puis appelle la fonction correspondante de
`operators.py`.

## 3. Installation (étape par étape)

Prérequis : **Python 3.10 ou plus récent**, **pip** et **Git**.

1. Cloner le dépôt :
   ```bash
   git clone <URL_DU_DEPOT>
   cd TP3---LOG3000
   ```
2. (Recommandé) Créer et activer un environnement virtuel :
   ```bash
   python -m venv .venv
   # Windows (PowerShell)
   .venv\Scripts\Activate.ps1
   # macOS / Linux
   source .venv/bin/activate
   ```
3. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## 4. Utilisation

### Lancer l'application

```bash
python app.py
```

Le serveur de développement démarre sur <http://127.0.0.1:5000>. Ouvrir cette
adresse dans un navigateur. Arrêter le serveur avec `Ctrl+C`.

### Utiliser la calculatrice

1. Cliquer sur les chiffres pour saisir le premier nombre (l'écran est en
   lecture seule : la saisie se fait uniquement avec les boutons).
2. Cliquer sur un opérateur : `+`, `-`, `*` ou `/`.
3. Saisir le second nombre.
4. Cliquer sur `=` : l'expression est envoyée au serveur et le résultat
   s'affiche dans l'écran (ex. `7*8` → `56.0`).
5. Cliquer sur `C` pour effacer l'écran.

Le résultat affiché peut servir d'opérande pour le calcul suivant
(ex. `-3.0` puis `+5` → `2.0`). Une expression invalide affiche
`Error: <raison>` ; appuyer sur `C` avant de recommencer.

## 5. Tests

La suite de tests utilise **pytest** et se trouve dans [`tests/`](tests/README.md).

```bash
# depuis la racine du dépôt
python -m pytest            # toute la suite
python -m pytest -v         # détail de chaque test
python -m pytest tests/test_operators.py   # un seul fichier
```

Les tests couvrent les opérations de `operators.py`, l'analyse des expressions
par `calculate()`, la route Flask et le contenu de l'interface HTML. Voir
`tests/README.md` pour le détail de la couverture.

## 6. Flux de contribution

Nous suivons un flux de type *GitHub Flow* :

1. **Issues** — tout bogue ou fonctionnalité commence par une issue GitHub qui
   décrit le problème, les étapes de reproduction (ou le test en échec) et le
   résultat attendu. L'issue est assignée à un membre de l'équipe.
2. **Branches** — une branche par issue, créée à partir de `main` à jour :
   - `fix/<num-issue>-<description-courte>` pour un bogue
     (ex. `fix/1-subtract-operand-order`) ;
   - `feature/<num-issue>-<description>` pour une fonctionnalité ;
   - `docs/<description>` pour la documentation.
   ```bash
   git switch main && git pull
   git switch -c fix/1-subtract-operand-order
   ```
3. **Commits** — messages à l'impératif, en anglais, qui expliquent *comment*
   la modification règle le problème, avec la référence `Fixes #<num>` pour
   fermer l'issue automatiquement à la fusion.
4. **Tests** — `python -m pytest` doit passer localement avant d'ouvrir une PR ;
   tout correctif est accompagné du test qui le démontre.
5. **Pull Requests** — une PR par branche vers `main`, qui référence l'issue,
   résume le correctif et montre le résultat des tests. Au moins un autre
   membre relit et approuve la PR avant la fusion.
6. **Fusion** — après approbation, fusionner la PR (merge commit), supprimer la
   branche, puis relancer la suite complète de tests sur `main`.

La branche `main` doit toujours rester dans un état où tous les tests passent.
