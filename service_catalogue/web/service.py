from flask import render_template
from service_catalogue.app import app
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import jsonify
import json


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


@app.route('/')
def index():
    app.logger.warning('sample message')
    return render_template('index.html')


@app.route("/service", methods=['GET', 'POST'])
def add_service():
    return "Add service."


@app.route("/service/<serviceId>", methods=['GET', 'PUT', 'DELETE'])
def service_actions(serviceId):

    # get
    client = MongoClient()
    db = client.test
    result = db.service.find({"_id" : ObjectId(serviceId)})

    data = [doc for doc in result]
    print(data)
    r = {
        'result': data,
        'message': "Get, modify and delete following service: {}".format(serviceId),
    }
    return JSONEncoder().encode(r)
