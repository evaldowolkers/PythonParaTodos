from flask import Flask
from my_app.teste.views import teste_blueprint

app = Flask(__name__)
app.register_blueprint(teste_blueprint)