from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/sucesso/<user_name>')
def success(user_name):
   return render_template('ola.html', user_name=user_name)

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user_name = request.form['user_name']
        if user_name == 'evaldo':
            return redirect(url_for('success', user_name = user_name))
        else:
            return "Usuário inválido."

if __name__ == '__main__':
   app.run(debug = True)