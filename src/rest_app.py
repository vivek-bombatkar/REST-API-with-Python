from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask.ext.jsonpify import jsonify

app = Flask(__name__)
api = Api(app)

class TestGet(Resource):
    def get(self):
        return {'result': ['test is successful!']}

class SumOfAllNumbers(Resource):
    def get(self): #,ip_list = list(range(10000001))
        ip_list = list(range(10000001))
        total = 0
        for i in ip_list:
            total =+ i
        return {'total': [total]}

api.add_resource(TestGet, '/testGet')

api.add_resource(SumOfAllNumbers, '/sumOfAllNumbers')  # /<ip_list>

if __name__ == '__main__':
    app.run(port=5002)