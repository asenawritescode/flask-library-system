from flask import Flask

# import config data from config.py
from configs import config

# Load all your extensions below ...
# Eg.
# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Configure the extensions below ...
    # Eg.
    # db.init_app(app)
    # bootstrap.init_app(app)

    # This is the main Blueprint
    # from .main.views import main as main_blueprint
    # app.register_blueprint(main_blueprint)
    # Register other Blueprints below ...
    
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