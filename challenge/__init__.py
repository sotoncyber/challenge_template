import os
from flask import Flask


app = Flask(__name__)
# app.config.from_object('config')

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

from challenge import views  # noqa: F401 E402
