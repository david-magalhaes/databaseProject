from flask import Flask
from flask_restful import Api, Resouce, reqparse

app = Flask(__name__)
api = Api(app)

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help='Field price is required')

    def get(self, name):
        data = Item.parser.parse_args()
        print(data['price'])
        return {'name': name, 'price': data['price']}

    def post(self, name):
        return {'name' : name}

api.add_resource(Item, '/item/<string:name>')
app.run(port=50001, hot='0.0.0.0', debug=True)
