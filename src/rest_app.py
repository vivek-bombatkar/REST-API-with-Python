from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

class sumOfAllNumbers(Resource):
    def get(self,list= list(range(10000001)) ):
        tmp = 0
        for i in list:
            tmp =+ i
        return tmp

api.add_resource(sumOfAllNumbers, "/test")

app.run(debug=True)