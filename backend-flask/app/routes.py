 from flask import render_template, jsonify
#from flask_restful import Resource, Api
from app import app
#api = Api(app)


@app.route('/')
@app.route('/index')
def index():
    return jsonify({"Home": "Hello World"})


@app.route('/character_creation')
def character_creation():
    return "This is a page to create characters"
