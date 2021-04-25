from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

app = Flask(__name__)
app.config['SECRET_KEY']="abc123"
app.config['SQLALCHEMY_DATABASE_URI']= "postgresql://yourusername:yourpassword@localhost/databasename"
db = SQLAlchemy(app)


app.config.from_object(Config)
from app import views