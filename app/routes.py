from app import api, web
from app.controllers import HelloController, MyViewController

api.add_resource(HelloController.MyController, '/')

web.add_resource(MyViewController.MyViewController, '/')
web.add_resource(MyViewController.MySecondViewController, '/say-my-name')