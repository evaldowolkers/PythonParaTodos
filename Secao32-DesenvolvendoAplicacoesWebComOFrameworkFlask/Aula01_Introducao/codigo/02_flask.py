from flask import Flask
app = Flask(__name__)

#@app.route("/teste")
def ola():
    return u'Olá mundo!'

app.add_url_rule("/", endpoint="ola", view_func=ola)

if __name__ == "__main__":
    app.run()