from flask import render_template
from service_catalogue.app import app


@app.route('/')
def index():
    app.logger.warning('sample message')
    return render_template('index.html')


@app.route("/hello")
def hello():
    return "Hello World!"
