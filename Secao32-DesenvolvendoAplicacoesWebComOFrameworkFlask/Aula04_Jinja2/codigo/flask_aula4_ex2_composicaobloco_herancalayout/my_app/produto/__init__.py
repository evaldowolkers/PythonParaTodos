from flask import Flask
from my_app.produto.views import product_blueprint

app = Flask(__name__)
app.register_blueprint(product_blueprint)