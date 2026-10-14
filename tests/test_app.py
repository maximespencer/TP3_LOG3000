"""Tests d'intégration de la route Flask ``/`` et du gabarit ``index.html``."""

import re

import pytest


def _button_labels(html):
    """Extrait le texte visible de chaque ``<button>`` de la page.

    Args:
        html (str): Code HTML de la page.

    Returns:
        list[str]: Libellés des boutons, dans l'ordre d'apparition.
    """
    return [label.strip() for label in re.findall(r"<button[^>]*>(.*?)</button>", html, re.S)]


def test_get_index_renders_calculator(client):
    """GET / retourne 200 et une page contenant l'écran vide."""
    resp = client.get("/")
    assert resp.status_code == 200
    assert b'id="display"' in resp.data
    assert b'value=""' in resp.data


@pytest.mark.parametrize("expr, shown", [
    ("2+3", "5.0"),
    ("10-4", "6.0"),
    ("6*7", "42.0"),
    ("9/2", "4.5"),
])
def test_post_displays_result(client, expr, shown):
    """POST / avec une expression affiche le bon résultat dans l'écran."""
    resp = client.post("/", data={"display": expr})
    assert resp.status_code == 200
    assert f'value="{shown}"' in resp.get_data(as_text=True)


def test_post_invalid_expression_shows_error(client):
    """Une expression invalide affiche un message d'erreur, pas une erreur 500."""
    resp = client.post("/", data={"display": "1+"})
    assert resp.status_code == 200
    assert 'value="Error:' in resp.get_data(as_text=True)


def test_button_labels_match_their_action(client):
    """Chaque bouton affiche le caractère qu'il ajoute à l'écran.

    Le libellé visible doit correspondre à l'argument de ``appendToDisplay``,
    sinon l'utilisateur ne sait pas ce qu'il saisit.
    """
    html = client.get("/").get_data(as_text=True)
    pairs = re.findall(r"appendToDisplay\('(.)'\)\">(.*?)</button>", html)
    assert len(pairs) == 14  # 10 chiffres + 4 opérateurs
    for value, label in pairs:
        assert label.strip() == value, f"button for {value!r} is labelled {label!r}"


def test_keypad_has_all_keys(client):
    """Le clavier contient exactement les 16 touches attendues."""
    labels = _button_labels(client.get("/").get_data(as_text=True))
    assert sorted(labels) == sorted(list("0123456789+-*/") + ["C", "="])
