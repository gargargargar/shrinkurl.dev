import os

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

import url_shrinker

app = Flask(__name__, instance_relative_config=True)
db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'GET':
        return render_template('index.html')
    
    url = request.form.get('url')
    result = url_shrinker.shrink_url(url)

    if result is None:
        return render_template('message.html',
            message='URL is not valid! (Hint: you might\'ve forgotten to include https:// or http://')
        
    return render_template('shrink_result.html',
        original_url=url,
        shrinked_url=request.url_root + result)

@app.route('/<shrinked_hash>')
def redirect(shrinked_hash):
    result = url_shrinker.redirect_shrinked_hash(shrinked_hash)

    if result is None:
        return render_template('message.html',
            message='This shrinkurl does not exist!')

    return render_template('redirect.html', url=result)

if __name__ == '__main__':
    app.run()