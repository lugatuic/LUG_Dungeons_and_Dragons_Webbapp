from flask import Flask

app = Flask(__name__)

from dnd_app import routes
