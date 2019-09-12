from flask import Flask, render_template, request,redirect, url_for, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        primeiro_nome = request.values.get('primeiro_nome')
        segundo_nome = request.values.get('segundo_nome')
        response = make_response(redirect(url_for('registrado')))
        response.set_cookie('primeiro_nome', primeiro_nome)
        response.set_cookie('segundo_nome', segundo_nome)
        return response
    return render_template('form.html')

@app.route('/obrigado')
def registrado():
    primeiro_nome = request.cookies.get('primeiro_nome')
    segundo_nome = request.cookies.get('segundo_nome')
    return f'Obrigado, {primeiro_nome} {segundo_nome}!'

if __name__ == '__main__':
    app.run()