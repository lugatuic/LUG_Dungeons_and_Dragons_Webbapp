"""Initialize Flask Server"""
from flask import Flask
from flask_mysqldb import MySQL
from flask_login import LoginManager
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
## Config mysql database.
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'test'
app.config['MYSQL_DB'] = 'lugdb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
## Config flask-login
login = LoginManager(app)

from dnd_app import routes
