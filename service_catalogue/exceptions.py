# -*- coding: utf-8 -*-

class ServiceBaseException(Exception):
    pass

class InvalidEnvironmentError(Exception):
    pass

class MissingRequiredArgumentException(ServiceBaseException):
    pass
