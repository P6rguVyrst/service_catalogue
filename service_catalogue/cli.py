# -*- coding: utf-8 -*-

"""Console script for service_catalogue."""
import sys
import click
from .service import ServiceInterface


# TODO:
#   - MongoDB
#   - Service architecture


@click.command()
@click.argument('method')
@click.option('--service_id')
@click.option('--data')
def main(method, **kwargs):
    """Console script for service_catalogue."""
    # click.echo("Replace this message by putting your code into "
    #           "service_catalogue.cli.main")
    # click.echo("See click documentation at http://click.pocoo.org/")

    service = ServiceInterface()
    router = {
        "add-service": service.add,
        "delete-service": service.delete,
        "get-service": service.get,
        "modify-service": service.modify,
    }
    args = [v for v in kwargs.values() if v]
    return router[method](*args)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
