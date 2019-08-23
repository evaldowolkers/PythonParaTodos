from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def exemplo():
    carros = ['Corolla', 'Sandero', 'Punto', 'Ranger', 'Gol', 'Clio', 'Ka']
    return render_template('exemplo.html', carros=carros)

if __name__ == '__main__':
    app.run()
