from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return u'Página principal!'

@app.route("/clientes/<funcao>")
def clientes(funcao):
    print("Função:", funcao)
    if(funcao.lower()=="cadastro"):
        return u'Cadastro de clientes!'
    elif(funcao.lower()=="consulta"):
        return u'Consulta de clientes!'
    elif(funcao.lower()=="alteracao"):
        return u'Alteração de clientes!'

if __name__ == "__main__":
    app.run()