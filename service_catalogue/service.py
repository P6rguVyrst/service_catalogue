# -*- coding: utf-8 -*-

"""Backend methods for handling service API requests."""

from pymongo import MongoClient
from bson.objectid import ObjectId
from .models import Service
from pprint import pprint as pp


'''
MONGO:
    insert_one
    insert_many
    delete_one
    delete_many
    find

'''


class ServiceInterface(object):

    def __init__(self):
        client = MongoClient()
        self.db = client.test
        self.db.service

    def get(self, serviceId):
        result = {
           'message': 'Get service with serviceId: {}'.format(serviceId),
           'service_object': self.db.service.find({"_id" : ObjectId(serviceId)}),
        }

        print(result)
        return result

    def add(self, data):
        # call service builder
        d = {
            'name': 'Logging service',
            'status': 'In Production',
            'environment': 'TEST',
            'business_owner': ['toomas.ormisson'],
            'technical_owner': ['toomas.ormisson'],
            'profit_center': 'IT',
            'cost_center': 'IT',
            'support_team': 'Infrastructure Team',
        }
        # TODO: Fix service object not to insert _ values to database.
        s = Service()
        s.name = d['name']
        s.status = d['status']
        #s.environment = d['']
        #s.status = d['']
        r = self.db.service.insert_one(s.__dict__)
        print(r.inserted_id)
        print(r.acknowledged)

        #pp(s.__dict__)

        result = {
            'message': 'Added a new service service',
            'data': data,
        }
        print(result)
        return result

    def modify(self, serviceId, data):

        result = {
            'message': 'Changed service with serviceId: {}'.format(data),
            'data': data,
        }
        print(result)
        return result

    def delete(self, serviceId):

        result = {
           'message': 'Deleted service with serviceId: {}'.format(serviceId),
        }
        print(result)
        return result
