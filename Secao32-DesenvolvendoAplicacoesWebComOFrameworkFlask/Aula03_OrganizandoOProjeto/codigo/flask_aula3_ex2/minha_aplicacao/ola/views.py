from minha_aplicacao import app
from minha_aplicacao.ola.models import MESSAGES

@app.route('/')
@app.route('/ola')
def ola_mundo():
    return MESSAGES.get['default']

@app.route('/show/<key>')
def get_message(key):
    return MESSAGES.get(key) or "%s not found!" % key

@app.route('/add/<key>/<message>')
def add_or_update_message(key, message):
    MESSAGES[key] = message
    return "%s Added/Updated" % key