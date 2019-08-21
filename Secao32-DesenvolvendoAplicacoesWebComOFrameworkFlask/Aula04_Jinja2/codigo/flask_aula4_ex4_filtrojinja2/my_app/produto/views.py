from werkzeug import abort
from flask import render_template
from flask import Blueprint
from my_app.produto.models import PRODUTOS
import ccy

product_blueprint = Blueprint('produto', __name__)

@product_blueprint.app_template_filter('nome_completo')
def nome_completo_filtro(produto):
    return '{0} / {1}'.format(produto['categoria'], produto['descricao'])

@product_blueprint.app_template_filter('formato_moeda')
def formato_moeda_filtro(valor):
    codigo_moeda = ccy.countryccy('BR')
    return '{0} {1}'.format(codigo_moeda, valor)

@product_blueprint.route('/')
@product_blueprint.route('/home')
def home():
    return render_template('home.html', produtos=PRODUTOS)

@product_blueprint.route('/produto/<key>')
def produto(key):
    produto = PRODUTOS.get(key)
    if not produto:
        return render_template('erro.html')
    return render_template('produto.html', produto=produto)