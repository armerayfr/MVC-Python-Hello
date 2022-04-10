from flask import Flask
from flask_restful import Api #call library RESTful

app = Flask(__name__, template_folder='views')
api = Api(app, prefix='/api') #initialize to library RESTful for route API
web = Api(app) #initialize to library RESTful for route web

from app import routes