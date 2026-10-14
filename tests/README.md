# `tests/` — Suite de tests automatisés

## Raison d'être

Vérifier automatiquement que la calculatrice produit les bons résultats et
détecter les régressions avant chaque fusion dans `main`.

## Exécuter les tests

Depuis la **racine** du dépôt (après `pip install -r requirements.txt`) :

```bash
python -m pytest              # toute la suite
python -m pytest -v           # affiche chaque test
python -m pytest tests/test_calculate.py            # un fichier
python -m pytest -k negative                        # tests dont le nom contient "negative"
```

`pytest.ini` (à la racine) ajoute la racine au `PYTHONPATH` : `app.py` et
`operators.py` sont importables sans installation.

## Fichiers et couverture

| Fichier | Niveau | Ce qui est couvert |
|---|---|---|
| `conftest.py` | — | Fixture `client` : client de test Flask (requêtes sans lancer de serveur). |
| `test_operators.py` | Unitaire | `add`, `subtract`, `multiply`, `divide` : résultat mathématique, ordre des opérandes, division réelle, division par zéro. |
| `test_calculate.py` | Unitaire | `app.calculate` : expressions valides, espaces, opérandes négatifs, expressions invalides (`ValueError`), division par zéro. |
| `test_app.py` | Intégration | Route `GET /` et `POST /` (résultat ou message d'erreur dans l'écran) ; libellés et composition du clavier dans `index.html`. |

## Hypothèses

- Les résultats sont des `float` (ex. `2+3` s'affiche `5.0`).
- Une seule opération par expression ; un `-` en tête d'opérande est un signe.
- Les tests HTML analysent le gabarit rendu avec des expressions régulières :
  ils supposent la forme `onclick="appendToDisplay('x')">libellé</button>`.

## Historique : tests en échec à l'origine

La première exécution sur le code fourni donnait **15 échecs / 30 tests**.
Chaque bogue a fait l'objet d'une issue GitHub et d'une branche de correction :

| Issue | Bogue | Tests qui échouaient | Branche |
|---|---|---|---|
| #1 | `subtract` calcule `b - a` | `test_subtract_order_matters`, `test_valid_expressions[10-4-6]`, `test_post_displays_result[10-4-6.0]` | `fix/1-subtract-operand-order` |
| #2 | `multiply` calcule `a ** b` | `test_multiply`, `test_valid_expressions[6*7-42]`, `test_post_displays_result[6*7-42.0]` | `fix/2-multiply-uses-power` |
| #3 | `divide` fait une division entière `//` | `test_divide_is_true_division`, `test_valid_expressions[9/2-4.5]`, `test_post_displays_result[9/2-4.5]` | `fix/3-divide-floor-division` |
| #4 | Libellés de boutons erronés (`02`, `88`, `*` et `/` vides) | `test_button_labels_match_their_action`, `test_keypad_has_all_keys` | `fix/4-keypad-button-labels` |
| #5 | Opérandes négatifs refusés (`-3+5` → erreur) | `test_negative_operands[*]` (4 cas) | `fix/5-negative-operands` |
