from flask import Flask, render_template, session, redirect, url_for
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
    form = NomeForm()
    if form.validate_on_submit():
        session['nome'] = form.nome.data
        return redirect(url_for('formulario'))
    return render_template('formulario.html', form=form, nome=session.get('nome'))

class NomeForm(FlaskForm):
    nome = StringField('Qual seu nome?', validators=[DataRequired()])
    submit = SubmitField('Enviar')


if __name__ == '__main__':
    app.run()
