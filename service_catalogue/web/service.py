from flask import render_template
from service_catalogue.app import app


@app.route('/')
def index():
    app.logger.warning('sample message')
    return render_template('index.html')


@app.route("/service", methods=['GET', 'POST'])
def add_service():
    return "Add service."


@app.route("/service/<serviceId>", methods=['GET', 'PUT', 'DELETE'])
def service_actions(serviceId):
    return "Get, modify and delete following service: {}".format(serviceId)
