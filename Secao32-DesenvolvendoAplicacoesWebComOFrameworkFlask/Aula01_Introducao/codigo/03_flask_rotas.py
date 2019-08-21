from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return u'Página principal!'

@app.route("/clientes")
def cadastro_clientes():
    return u'Página de clientes!'

@app.route("/fornecedores")
def cadastro_fornecedores():
    return u'Página de fornecedores!'

if __name__ == "__main__":
    app.run()