from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# import config data from config.py
from configs import config

# Load all your extensions below ...
# Eg.

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Configure the extensions below ...
    # Eg.
    db.init_app(app)

    # Load utility functions below ...
    # Eg.
    # from .utils import *
    # 

    # Register your blueprints here ...
    
    from .services.main import main_bp
    app.register_blueprint(main_bp)

    from .services.books import book_bp
    app.register_blueprint(book_bp)

    from .services.transactions import transactions_bp
    app.register_blueprint(transactions_bp)

    from .services.users import users_bp
    app.register_blueprint(users_bp)

    from .services.reports import reports_bp
    app.register_blueprint(reports_bp)

    return app