"""Initialize Flask Server"""
from flask import Flask

from dnd_app import routes

app = Flask(__name__)
