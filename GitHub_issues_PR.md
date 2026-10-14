# Textes à copier dans GitHub

**Ordre important :** créer les 5 issues (#1 à #5) AVANT d'ouvrir les PR, pour que
les numéros correspondent aux `Fixes #N` des commits (la fusion de la PR fermera
alors l'issue automatiquement). Assigner chaque issue à un membre.

---

## Issue #1 — `subtract` inverse l'ordre des opérandes

**Description**
`operators.subtract(a, b)` retourne `b - a` au lieu de `a - b`. Toute soustraction
saisie dans la calculatrice donne le résultat de signe opposé.

**Étapes de reproduction**
1. `python app.py`, ouvrir http://127.0.0.1:5000
2. Saisir `10-4` puis `=`
3. Résultat obtenu : `-6.0` — attendu : `6.0`

**Tests en échec**
- `tests/test_operators.py::test_subtract_order_matters` (`assert -7 == 7`)
- `tests/test_calculate.py::test_valid_expressions[10-4-6]`
- `tests/test_app.py::test_post_displays_result[10-4-6.0]`

**Correctif proposé** : `return a - b` dans `operators.py`.
**Labels** : bug — **Assigné à** : …

---

## Issue #2 — `multiply` calcule une puissance

**Description**
`operators.multiply(a, b)` utilise `a ** b` (exponentiation) au lieu de `a * b`.

**Étapes de reproduction**
1. Saisir `6*7` puis `=`
2. Résultat obtenu : `279936.0` (6⁷) — attendu : `42.0`

**Tests en échec**
- `tests/test_operators.py::test_multiply` (`assert 81 == 12`)
- `tests/test_calculate.py::test_valid_expressions[6*7-42]`
- `tests/test_app.py::test_post_displays_result[6*7-42.0]`

**Correctif proposé** : `return a * b`.
**Labels** : bug — **Assigné à** : …

---

## Issue #3 — `divide` fait une division entière

**Description**
`operators.divide(a, b)` utilise `//` (division entière, arrondie vers −∞) au lieu
de `/`. La partie décimale est perdue et les négatifs sont mal arrondis.

**Étapes de reproduction**
1. Saisir `9/2` puis `=`
2. Résultat obtenu : `4.0` — attendu : `4.5`

**Tests en échec**
- `tests/test_operators.py::test_divide_is_true_division` (`assert 3 == 3.5`)
- `tests/test_calculate.py::test_valid_expressions[9/2-4.5]`
- `tests/test_app.py::test_post_displays_result[9/2-4.5]`

**Correctif proposé** : `return a / b`.
**Labels** : bug — **Assigné à** : …

---

## Issue #4 — Libellés des boutons du clavier erronés ou manquants

**Description**
Dans `templates/index.html`, le libellé de plusieurs boutons ne correspond pas au
caractère qu'ils ajoutent : le bouton `2` affiche « 02 », le bouton `8` affiche
« 88 », et les boutons `*` et `/` n'ont aucun libellé (touches orange vides).

**Étapes de reproduction**
1. Ouvrir http://127.0.0.1:5000
2. Observer le clavier : « 02 », « 88 » et deux touches orange vides.

**Tests en échec**
- `tests/test_app.py::test_button_labels_match_their_action`
- `tests/test_app.py::test_keypad_has_all_keys`

**Correctif proposé** : libellés `2`, `8`, `*`, `/`.
**Labels** : bug, frontend — **Assigné à** : …

---

## Issue #5 — Les opérandes négatifs sont refusés

**Description**
`app.calculate` considère tout `+`/`-` comme l'opérateur binaire. Une expression
commençant par un nombre négatif est donc rejetée. Cas réel : après `2-5`, l'écran
affiche un résultat négatif ; enchaîner `+5` donne `-3.0+5` → erreur.

**Étapes de reproduction**
1. Saisir `-3+5` (ou réutiliser un résultat négatif) puis `=`
2. Résultat obtenu : `Error: only one operator is allowed` — attendu : `2.0`

**Tests en échec**
- `tests/test_calculate.py::test_negative_operands[*]` (5 cas : `-3+5`, `-3.0+1.5`,
  `5+-2`, `-1+-1`, `1e-05+1`)

**Correctif proposé** : ne reconnaître un symbole comme opérateur binaire que s'il
suit un chiffre ou un point ; sinon c'est le signe de l'opérande.
**Labels** : bug — **Assigné à** : …

---

# Pull Requests (une par branche, base : `main`)

Ordre de fusion conseillé : #1, #2, #3, #4, #5 (aucun conflit : vérifié localement).
Après chaque fusion : `git switch main && git pull && python -m pytest`.

### PR — `fix/1-subtract-operand-order`
**Titre** : Fix subtract operand order (Fixes #1)
**Description** : `subtract` retournait `b - a` ; il retourne maintenant `a - b`.
Tests : `test_subtract_order_matters`, `test_valid_expressions[10-4-6]`,
`test_post_displays_result[10-4-6.0]` passent (3 passed).
Closes #1

### PR — `fix/2-multiply-uses-power`
**Titre** : Fix multiply using exponentiation (Fixes #2)
**Description** : remplace `a ** b` par `a * b`. Tests : `test_multiply` et les
cas `6*7` passent (3 passed).
Closes #2

### PR — `fix/3-divide-floor-division`
**Titre** : Fix divide using floor division (Fixes #3)
**Description** : remplace `//` par `/` ; la division par zéro lève toujours
`ZeroDivisionError`. Tests : `test_divide_is_true_division`, les cas `9/2` et
`test_divide_by_zero_raises` passent.
Closes #3

### PR — `fix/4-keypad-button-labels`
**Titre** : Fix wrong and missing keypad button labels (Fixes #4)
**Description** : libellés `02`→`2`, `88`→`8`, ajout de `*` et `/`.
Tests : `test_button_labels_match_their_action`, `test_keypad_has_all_keys` passent.
Closes #4

### PR — `fix/5-negative-operands`
**Titre** : Accept signed operands in calculate (Fixes #5)
**Description** : un `+`/`-` n'est l'opérateur binaire que s'il suit un chiffre ou
un point ; sinon c'est le signe de l'opérande. Les expressions invalides restent
rejetées. Tests : `test_negative_operands` (5 cas) et
`test_invalid_expressions_raise_value_error` (7 cas) passent (13 passed).
Closes #5

**Résultat attendu après les 5 fusions** : `python -m pytest` → `31 passed`.
