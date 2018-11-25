from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask.ext.jsonpify import jsonify
import json
app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()

class TestGet(Resource):
    """
    A test rest function!
    Returns:
        result: JSON as success message!
    """
    def get(self):
        return {'result': ['test is successful!']}

class SumOfAllNumbers(Resource):
    """
    Calculates sun of all the numbers
    Returns:
        total : JSON with total of the numbers.
    """
    def get(self):
        ip_list = list(range(10000001))
        total = 0
        for i in ip_list:
            total =+ i
        return {'total': [total]}

api.add_resource(TestGet, '/testGet')
api.add_resource(SumOfAllNumbers, '/sumOfAllNumbers')

if __name__ == '__main__':
    app.run(port=5002)