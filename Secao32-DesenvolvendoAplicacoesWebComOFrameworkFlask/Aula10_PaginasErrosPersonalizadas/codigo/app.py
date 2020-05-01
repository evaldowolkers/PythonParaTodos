from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pagina2')
def pagina2():
    return render_template('pagina2.html')


@app.errorhandler(404)
def pagina_nao_encontrada(e):
    return render_template('404.html')

@app.errorhandler(500)
def pagina_erro_sistema(e):
    return render_template('500.html')

@app.route('/gerar_erro')
def gerar_erro():
    a = 'Teste'
    b = 10
    c = a + b
    return c

if __name__ == '__main__':
    app.run()
