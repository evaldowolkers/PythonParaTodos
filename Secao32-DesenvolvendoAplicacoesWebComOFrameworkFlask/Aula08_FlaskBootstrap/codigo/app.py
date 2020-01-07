from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/exemplo')
def exemplo():
    return render_template('exemplo.html', nome="Evaldo")

if __name__ == '__main__':
    app.run()