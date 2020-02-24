from flask import Flask, request
from flask_restful import Resource, Api
import socket

app = Flask(__name__)
api = Api(app)

class Greeting (Resource):
    def get(self):
        try:
            host_name = socket.gethostname()
            host_ip = socket.gethostbyname(host_name)
            message = "Hostname :  "+ host_name + "IP : " + host_ip
            return message
        except:
            return 'Sorry! Something is not right, let me look into it!'

api.add_resource(Greeting, '/') # Route_1
if __name__ == '__main__':
    app.run('0.0.0.0','8080')
