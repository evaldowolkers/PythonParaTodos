from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'string_chave_secreta'
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def principal():
    return render_template('principal.html')

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    nome = None
    form = NomeForm()
    if form.validate_on_submit():
        nome = form.nome.data
        form.nome.data = ''
    return render_template('formulario.html', form=form, nome=nome)

class NomeForm(FlaskForm):
    nome = StringField('Qual seu nome?', validators=[DataRequired()])
    submit = SubmitField('Enviar')


if __name__ == '__main__':
    app.run()
