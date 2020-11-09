import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import url_shrinker

app = Flask(__name__, instance_relative_config=True)
db = SQLAlchemy(app)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/<shrinked_hash>')
def redirect(shrinked_hash):
    result = url_shrinker.redirect_shrinked_hash(shrinked_hash)

    if result is None:
        return 'Url does not exist!'

    return result

if __name__ == '__main__':
    app.run()