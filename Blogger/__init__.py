from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .helpers import has_error

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_message_category = "is-info"
login_manager.login_view = "auth_app.login"


def create_app(**config_overrides):
    app = Flask(__name__)

    # Load config
    app.config.from_pyfile('settings.py')

    # Apply config overrides for test
    app.config.update(**config_overrides)

    # Initialize db
    db.init_app(app)
    Migrate(app, db)

    login_manager.init_app(app)

    # Import Blueprints
    from .auth.views import auth_app
    from .users.views import users_app

    # Register Blueprints
    app.register_blueprint(auth_app)
    app.register_blueprint(users_app)

    app.add_template_global(has_error, name='has_error')

    return app
