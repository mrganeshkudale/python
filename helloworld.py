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
        print("Hostname :  ",host_name) 
        print("IP : ",host_ip) 
      except: 
        print("Unable to get Hostname and IP") 
        
      return 'Hello Docker World Again!'

api.add_resource(Greeting, '/') # Route_1

if __name__ == '__main__':
    app.run('0.0.0.0','3333')
