
from flask import Flask

#creates instance of the flask class
#name is a place holder for the current module
app = Flask(__name__)

from app import routes

if __name__ == '__main__':
    app.run(debug=True)
