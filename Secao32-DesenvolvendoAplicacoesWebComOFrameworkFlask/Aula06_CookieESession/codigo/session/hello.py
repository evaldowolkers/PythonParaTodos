from flask import Flask, render_template, request,redirect, url_for, session

app = Flask(__name__)

app.secret_key = "minha_chave_secreta"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        primeiro_nome = request.values.get('primeiro_nome')
        segundo_nome = request.values.get('segundo_nome')
        session['primeiro_nome'] = primeiro_nome
        session['segundo_nome'] = segundo_nome
        return redirect(url_for('registrado'))
    return render_template('form.html')

@app.route('/obrigado')
def registrado():
    primeiro_nome = session.get('primeiro_nome')
    segundo_nome = session.get('segundo_nome')
    return f'Obrigado, {primeiro_nome} {segundo_nome}!'

if __name__ == '__main__':
    app.run()