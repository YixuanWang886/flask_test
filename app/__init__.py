from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.debug=True
app.config['SECRET_KEY'] = 'your-secret-key'
app.debug=True
login=LoginManager(app)
login.login_view = 'login'

app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'
db=SQLAlchemy(app)
migrate=Migrate(app,db)

from app import routes, models