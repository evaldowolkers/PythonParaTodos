from flask import Blueprint
from flask import render_template

teste_blueprint = Blueprint('teste', __name__)

@teste_blueprint.route('/')
def teste():
    return render_template('teste.html')