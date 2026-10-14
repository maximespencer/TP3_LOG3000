"""Point d'entrée de l'application web de calculatrice.

Ce module crée l'application Flask, expose la route ``/`` qui affiche
l'interface (``templates/index.html``) et évalue les expressions soumises
par le formulaire. L'analyse d'une expression est faite par ``calculate`` et
le calcul lui-même est délégué aux fonctions de ``operators.py``.

Lancement : ``python app.py`` (serveur de développement sur le port 5000).
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

# Table de correspondance symbole -> fonction. Elle sert aussi de liste des
# caractères reconnus comme opérateurs lors de l'analyse de l'expression.
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculate(expr: str):
    """Évalue une expression binaire simple de la forme ``<nombre><op><nombre>``.

    Les espaces sont ignorés. Une seule opération est permise par expression
    (pas de priorité d'opérateurs ni de parenthèses). Les opérandes peuvent
    être signés (``"-3+5"``, ``"5*-2"``), ce qui permet de réutiliser un
    résultat négatif affiché à l'écran.

    Args:
        expr (str): L'expression saisie, par exemple ``"12.5 * 4"``.

    Returns:
        float: Le résultat de l'opération.

    Raises:
        ValueError: Si l'expression est vide, contient plus d'un opérateur,
            n'a pas d'opérande de part et d'autre de l'opérateur, ou si un
            opérande n'est pas un nombre.
        ZeroDivisionError: En cas de division par zéro.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    for i, ch in enumerate(s):
        # Un symbole n'est l'opérateur binaire que s'il suit la fin d'un
        # nombre (chiffre ou point). Sinon (début de chaîne, après un autre
        # opérateur ou après le "e" d'une notation scientifique), c'est le
        # signe de l'opérande : "-3+5", "5*-2", "1e-05+1".
        if ch in OPS and i > 0 and (s[i-1].isdigit() or s[i-1] == '.'):
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    # Un opérateur en première ou dernière position signifie qu'il manque un
    # opérande ; -1 signifie qu'aucun opérateur n'a été trouvé.
    if op_pos <= 0 or op_pos >= len(s) - 1:
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)


@app.route('/', methods=['GET', 'POST'])
def index():
    """Affiche la calculatrice et, sur POST, le résultat du calcul.

    Entrée (POST) : champ de formulaire ``display`` contenant l'expression.

    Returns:
        str: La page HTML rendue ; la variable ``result`` contient le résultat
        du calcul, un message ``"Error: ..."`` en cas d'échec, ou une chaîne
        vide sur GET.
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            # L'erreur est affichée dans l'écran de la calculatrice plutôt
            # que de produire une erreur HTTP 500.
            result = f"Error: {e}"
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
