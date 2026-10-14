"""Tests unitaires des fonctions arithmétiques de ``operators.py``.

Chaque fonction est vérifiée contre l'opération mathématique attendue
``a <op> b``, avec des opérandes choisis pour que les implémentations
erronées plausibles (opérandes inversés, puissance, division entière)
donnent un résultat différent.
"""

import pytest

from operators import add, subtract, multiply, divide


def test_add():
    """``add`` retourne la somme, y compris avec négatifs et décimaux."""
    assert add(2, 3) == 5
    assert add(-4, 1.5) == -2.5


def test_subtract_order_matters():
    """``subtract(a, b)`` doit retourner ``a - b`` et non ``b - a``."""
    assert subtract(10, 3) == 7
    assert subtract(3, 10) == -7


def test_multiply():
    """``multiply`` doit retourner le produit (3*4 = 12, alors que 3**4 = 81)."""
    assert multiply(3, 4) == 12
    assert multiply(2.5, -2) == -5


def test_divide_is_true_division():
    """``divide`` doit faire une division réelle : 7/2 = 3.5 (et non 3)."""
    assert divide(7, 2) == 3.5
    assert divide(-7, 2) == -3.5


def test_divide_by_zero_raises():
    """La division par zéro doit lever une exception plutôt que retourner une valeur."""
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
