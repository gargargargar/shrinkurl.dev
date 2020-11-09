import os

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

import url_shrinker

app = Flask(__name__, instance_relative_config=True)
db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return render_template('index.html')
    
    url = request.form.get('url')
    result = url_shrinker.shrink_url(url)

    if result is None:
        return 'URL is not valid!'
    return result

@app.route('/<shrinked_hash>')
def redirect(shrinked_hash):
    result = url_shrinker.redirect_shrinked_hash(shrinked_hash)

    if result is None:
        return 'URL does not exist!'

    return result

if __name__ == '__main__':
    app.run()