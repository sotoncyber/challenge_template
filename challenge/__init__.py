from flask import Flask

app = Flask(__name__)
# app.config.from_object('config')

from challenge import views  # noqa: F401 E402
