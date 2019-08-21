from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/admin')
def ola_admin():
   return 'Olá Admin'

@app.route('/visitante/<visitante>')
def ola_visitante(visitante):
   return 'Olá %s visitante' % visitante

@app.route('/usuario/<nome>')
def ola_user(nome):
   if nome =='admin':
      return redirect(url_for('ola_admin'))
   else:
      return redirect(url_for('ola_visitante',visitante = nome))

if __name__ == '__main__':
   app.run(debug = True)