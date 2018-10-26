import os
from flask import Flask


app = Flask(__name__)
app.config.from_object('service_catalogue.default_settings')
app.config.from_envvar('SERVICE_CATALOGUE_SETTINGS')


if not app.debug:
    import logging
    from logging.handlers import TimedRotatingFileHandler
    # https://docs.python.org/3.6/library/logging.handlers.html#timedrotatingfilehandler
    file_handler = TimedRotatingFileHandler(
        os.path.join(
            app.config['LOG_DIR'],
            'service_catalogue.log'
        ), 'midnight')
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(
        logging.Formatter('<%(asctime)s> <%(levelname)s> %(message)s'))
    app.logger.addHandler(file_handler)

import service_catalogue.web.service


if __name__ == "__main__":
    app.run()
