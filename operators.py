"""Opérations arithmétiques de base utilisées par la calculatrice.

Chaque fonction reçoit deux opérandes numériques (``float`` en pratique, car
``app.calculate`` convertit les opérandes avant l'appel) et retourne le résultat
de l'opération ``a <op> b``. L'ordre des opérandes est significatif : ``a`` est
toujours l'opérande de gauche saisi par l'utilisateur.
"""


def add(a, b):
    """Additionne deux nombres.

    Args:
        a (float): Opérande de gauche.
        b (float): Opérande de droite.

    Returns:
        float: La somme ``a + b``.
    """
    return a + b


def subtract(a, b):
    """Soustrait l'opérande de droite de l'opérande de gauche.

    Args:
        a (float): Opérande de gauche (diminuende).
        b (float): Opérande de droite (diminuteur).

    Returns:
        float: La différence ``a - b``.
    """
    return b - a


def multiply(a, b):
    """Multiplie deux nombres.

    Args:
        a (float): Opérande de gauche.
        b (float): Opérande de droite.

    Returns:
        float: Le produit ``a * b``.
    """
    return a * b


def divide(a, b):
    """Divise l'opérande de gauche par l'opérande de droite (division réelle).

    Args:
        a (float): Dividende.
        b (float): Diviseur.

    Returns:
        float: Le quotient ``a / b``.

    Raises:
        ZeroDivisionError: Si ``b`` vaut 0.
    """
    return a // b
