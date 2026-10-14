"""Tests de ``app.calculate`` : analyse d'une expression et dispatch vers l'opérateur."""

import pytest

from app import calculate


@pytest.mark.parametrize("expr, expected", [
    ("2+3", 5),
    ("10-4", 6),
    ("6*7", 42),
    ("9/2", 4.5),
    (" 1.5 + 2.25 ", 3.75),  # les espaces sont ignorés
])
def test_valid_expressions(expr, expected):
    """Une expression binaire valide retourne le résultat mathématique attendu."""
    assert calculate(expr) == pytest.approx(expected)


@pytest.mark.parametrize("expr, expected", [
    ("-3+5", 2),        # résultat négatif réutilisé comme premier opérande
    ("-3.0+1.5", -1.5),
    ("5+-2", 3),        # opérande de droite négatif
    ("-1+-1", -2),      # deux opérandes négatifs
    ("1e-05+1", 1.00001),  # le "-" de la notation scientifique n'est pas un opérateur
])
def test_negative_operands(expr, expected):
    """Un signe ``-`` en tête d'opérande est un signe, pas un second opérateur.

    Cas réel : après ``2-5 = -3.0``, l'utilisateur enchaîne ``+5`` à l'écran.
    Seule l'addition est utilisée pour isoler l'analyse de l'expression du
    comportement des autres opérateurs (testés dans ``test_operators.py``).
    """
    assert calculate(expr) == pytest.approx(expected)


@pytest.mark.parametrize("expr", ["", "5", "+5", "5+", "1+2+3", "a+1", "1+b"])
def test_invalid_expressions_raise_value_error(expr):
    """Les expressions mal formées lèvent ``ValueError`` avec un message explicite."""
    with pytest.raises(ValueError):
        calculate(expr)


def test_division_by_zero():
    """La division par zéro n'est pas silencieuse."""
    with pytest.raises(ZeroDivisionError):
        calculate("1/0")
