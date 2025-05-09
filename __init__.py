from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from .config import Config
from flask_mail import Mail
import os

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
mail = Mail(app) # Inizializzazione di mail

from .models import User, Material, ProductBrand, ProductCategory

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from . import routes
