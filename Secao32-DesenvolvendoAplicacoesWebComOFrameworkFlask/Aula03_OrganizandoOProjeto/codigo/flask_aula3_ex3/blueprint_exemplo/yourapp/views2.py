from flask import Blueprint

views2 = Blueprint('views2', __name__)

@views2.route('/teste')
def teste():
	return '<h1>Esta é a segunda view!</h1>'