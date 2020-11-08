import os

from flask import Flask

app = Flask(__name__, instance_relative_config=True)
# def create_app(test_config=None):
#     # create and configure the app
#     app.config.from_mapping(
#         SECRET_KEY='dev',
#         DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
#     )

#     if test_config is None:
#         # load the instance config, if it exists, when not testing
#         app.config.from_pyfile('config.py', silent=True)
#     else:
#         # load the test config if passed in
#         app.config.from_mapping(test_config)

#     # ensure the instance folder exists
#     try:
#         os.makedirs(app.instance_path)
#     except OSError:
#         pass

#     return app

# a simple page that says hello
@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/<short_url>')
def redirect(short_url):
    # show the post with the given id, the id is an integer
    return short_url

if __name__ == '__main__':
    # create_app()
    app.run()