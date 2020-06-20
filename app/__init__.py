import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import basedir
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'auth'
login_manager.login_message = 'Пожалуйста введите email и пароль'

from app import views , models