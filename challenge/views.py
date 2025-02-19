import flask
from challenge import app, forms
from flask import render_template


@app.route('/', methods=['GET'])
def index() -> str:
    return render_template("index.html")

@app.route('/1', methods=['GET'])
def ch_1() -> str:
    return render_template("challenge1.html")

@app.route('/2', methods=['GET', 'POST'])
def ch_2() -> str:
    form = forms.LoginForm()
    if flask.request.method == 'POST':
        if form.username.data == "admin" and form.password.data == "admin":
            return render_template("challenge2.html", form=form, response="flag{some-flag-idk-lol}")
        else:
            return render_template("challenge2.html", form=form, response="Incorrect username/password")
    return render_template("challenge2.html", form=form)

