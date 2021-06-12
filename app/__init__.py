from flask import Flask

from config import Config

#import for flask DB and Migrator
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#import for flask login
from flask_login import LoginManager

#Import for Flask Mail
from flask_mail import Mail, Message


#Create intance of Flask class, name it app
app = Flask(__name__)
#Add configurations
app.config.from_object(Config)


# Create db and migrator
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Login 
login = LoginManager(app)
login.login_view = 'login' #specify what page to laod for non-authencated users

#Mail
mail = Mail(app)

from app import routes, models
