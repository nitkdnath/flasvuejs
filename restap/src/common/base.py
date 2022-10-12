from flask_mysqldb import MySQL
#from src.controller.app import app
from flask import Flask
import pymysql
from flask_cors import CORS
app = Flask(__name__)
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:2176@localhost:3306/inventory'
app.config["SECRET_KEY"] = "restapi"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] =  False
db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)
