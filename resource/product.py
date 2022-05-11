import json

from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from pydantic import BaseModel, ValidationError

from models import products


class ProductSchema(BaseModel):
    name: str
    notes: str
    producer_edrpou: int
    category_id: int
    price: int


class Products(Resource):
    # @jwt_required()
    def get(self):
        products_tpl = products.get_products()
        products_out = []
        for product_tpl in products_tpl:
            product_dict = {
                "id": product_tpl[0],
                "name": product_tpl[1],
                "notes": product_tpl[2],
                "producer_edrpou": product_tpl[3],
                "category_id": product_tpl[4],
                "price": product_tpl[5]
            }
            products_out.append(product_dict)
        return products_out


class Product(Resource):

    # @jwt_required()
    def get(self, _id):
        product_tpl = products.get_product_by_id(_id)
        json_out = {
            "id": product_tpl[0],
            "name": product_tpl[1],
            "notes": product_tpl[2],
            "producer_edrpou": product_tpl[3],
            "category_id": product_tpl[4],
            "price": product_tpl[5]
        }
        return json_out

    # @jwt_required()
    def post(self):
        try:
            product_schema = ProductSchema.parse_raw(json.dumps(request.get_json()))
        except ValidationError:
            return {"message": "invalid arguments"}

        _id = products.add_new_product(product_schema.name, product_schema.notes, product_schema.producer_edrpou,
                                       product_schema.category_id, product_schema.price)
        return {"id": _id}

    # @jwt_required()
    def delete(self, _id):
        return products.delete_product(_id)
