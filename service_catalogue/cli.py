# -*- coding: utf-8 -*-

"""Console script for service_catalogue."""
import sys
import click

#TODO:
#   - Flask API
#   - MongoDB
#   - Service architecture



@click.command()

def main(args=None):
    """Console script for service_catalogue."""
    click.echo("Replace this message by putting your code into "
               "service_catalogue.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")

    router =  {
        "add-service": None,
        "remove-service": None,
        "show-service": None,
    }


    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
