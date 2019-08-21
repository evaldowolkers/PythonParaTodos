from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<user_name>')
def success(user_name):
    return 'Bem-vindo %s' % user_name

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user_name = request.form['user_name']
        return redirect(url_for('success', user_name = user_name))
    else:
        user_name = request.args.get('user_name')
        return redirect(url_for('success', user_name = user_name))

if __name__ == '__main__':
    app.run()