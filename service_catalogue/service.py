# -*- coding: utf-8 -*-

"""Backend methods for handling service API requests."""

from pymongo import MongoClient


class Service(object):

    def __init__(self):
        client = MongoClient()
        self.db = client.admin

    def get(self, serviceId):
        tstt = self.db.command("serverStatus")
        result = {
           'message': 'Get service with serviceId: {}'.format(serviceId),
           'db_status': tst,
        }
        print(result)
        return result

    def add(self, data):

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
