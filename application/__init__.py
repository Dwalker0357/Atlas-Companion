from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://d_walker0357:password@localhost/exile'

db = SQLAlchemy(app)

from application import routes
