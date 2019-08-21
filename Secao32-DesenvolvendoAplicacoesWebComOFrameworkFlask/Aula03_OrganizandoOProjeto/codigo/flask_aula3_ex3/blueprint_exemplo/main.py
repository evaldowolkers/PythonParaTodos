from flask import Flask
from yourapp.views import views
from yourapp.views2 import views2

app = Flask(__name__)
app.register_blueprint(views)
app.register_blueprint(views2)

if __name__ == '__main__':
	app.run()