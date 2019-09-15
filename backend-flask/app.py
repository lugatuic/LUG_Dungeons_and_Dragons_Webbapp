from flask import Flask, jsonify
from flask import Blueprint
from flask_restful import Api

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"


if __name__ == '__main__':
    app.run(debug=True)
