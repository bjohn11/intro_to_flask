from flask import Flask

from config import Config

#import for flask DB and Migrator
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#import for flask login
from flask_login import LoginManager

#Import for Flask Mail
from flask_mail import Mail, Message


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app)
    mail.init_app(app)

    login.init_app(app)
    login.login_view = 'login'
    with app.app_context():
        from . import routes, models

        from app.blueprints.auth import bp as auth
        app.register_blueprint(auth)

        from app.blueprints.blog import bp as blog
        app.register_blueprint(blog)
        
    return app
  
