
import click
# from flask_migrate import Migrate
from app import create_app, db

from app.models import *



@click.group()
def cli():
    pass


@click.command()
@click.option(
    '--env', default='development',
    help='Environment to use while running server',
    type=click.STRING
)
@click.option(
    '--port', default=5000,
    help='Port to use while running server',
    type=click.STRING
)
def runserver(env, port):
    app = create_app(env)
    # print('Running Server {env}'.format(env=env))
    with app.app_context():
        db.create_all()
    app.run(port=port)

# cli command to run tests
@click.command()
def runtest():
    """Testing """
    import unittest
    import sys

    tests = unittest.TestLoader().discover("tests")

    results = unittest.TextTestRunner(verbosity=3).run(tests)

    if not results.wasSuccessful():

        sys.exit(1)

# @click.command()
# @click.option(
#     '--env', default='development',
#     help='Environment to use while running server',
#     type=click.STRING
# )
# def migrate(env):    
#     create_app(env)
#     # Migrate(app, db)
#     print('Running Migrations')

# @click.command()
# @click.option(
#     '--env', default='development',
#     help='Environment to use while running server',
#     type=click.STRING
# )
# def init_db(env):
#     app = create_app(env)
#     db.create_all(app)
#     return

cli.add_command(runserver)
cli.add_command(runtest)
# cli.add_command(init_db)
# cli.add_command(migrate)

if __name__ == "__main__":
    cli()