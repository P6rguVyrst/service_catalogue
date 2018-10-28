# -*- coding: utf-8 -*-
from .exceptions import (
    InvalidEnvironmentError,
    MissingRequiredArgumentException,
)
import json

class ServiceVerifier(object):

    def verify_environment(self, env):
        accepted_values = [
            "DEV",
            "TEST",
            "LIVE",
        ]
        if env not in accepted_values:
            raise InvalidEnvironmentError()

    def verify_service_name(self, name):
        if not name:
            raise MissingRequiredArgumentException("Missing name")

    def verify_service_status(self, status):
        if not status:
            raise MissingRequiredArgumentException("Missing name")


class MyEncoder(json.JSONEncoder):
    def default(self, o):
        return {k.lstrip('_'): v for k, v in vars(o).items()}

class Service(ServiceVerifier):

    def __init__(self):
        #self.verify = ServiceVerifier()
        self._name = None
        self._status = "In development"
        self._environment = "DEV"
        self._business_owner = []
        self._technical_owner = []
        self._profit_center = None
        self._cost_center = None
        self._support_team = None

    # name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self.verify_service_name(value)
        self._name = value

    @name.deleter
    def name(self):
        del self._name

    # status
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self.verify.service_status(value)
        self._status = value

    @status.deleter
    def status(self):
        del self._status

    def to_dict(self):
        # TODO: do better, without having to declare all service properties here.
        return {
            'name': self._name,
            'status': self._status,
            'environment': self._environment,
            'business_owner': self._business_owner,
            'technical_owner': self._technical_owner,
            'profit_center': self._profit_center,
            'cost_center': self._cost_center,
            'support_team': self._support_team,
        }
