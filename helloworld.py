from flask import Flask, request
from flask_restful import Resource, Api
import socket

app = Flask(__name__)
api = Api(app)

class Greeting (Resource):
    def get(self):
      message = "Welcome back, greetings from "+socket.gethostname()+"!"
      return message 

api.add_resource(Greeting, '/') # Route_1

if __name__ == '__main__':
    app.run('0.0.0.0','3333')
