from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resource.product import Product, Products
from resource.category import Category, Categories
from resource.customer import Customer, Customers
from resource.order import Order, Orders
from resource.producer import Producer, Producers

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.secret_key = '1234'
api = Api(app)


api.add_resource(Product, '/product', '/product/<int:_id>')
api.add_resource(Products, '/products')
api.add_resource(Category, '/category', '/category/<int:_id>')
api.add_resource(Categories, '/categories')
api.add_resource(Customer, '/customer', '/customer/<int:ipn>')
api.add_resource(Customers, '/customers')
api.add_resource(Order, '/order', '/order/<int:_id>')
api.add_resource(Orders, '/orders')
api.add_resource(Producer, '/producer', '/producer/<int:edrpou>')
api.add_resource(Producers, '/producers')


jwt = JWTManager(app)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
