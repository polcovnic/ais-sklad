import json
from typing import Optional

from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from pydantic import BaseModel, ValidationError

from models import customers


class CustomerSchema(BaseModel):
    ipn: int
    surname: str
    name: str
    patronymic: str
    phone_number: str
    country: str
    state: str
    city: str
    street: str
    house_number: int
    email: str
    debt: str
    notes: Optional[str]


class Customers(Resource):
    # @jwt_required()
    def get(self):
        customers_tpl = customers.get_customers()
        customers_out = []
        for customer_tpl in customers_tpl:
            category_dict = {
                "ipn": customer_tpl[0],
                "notes": customer_tpl[1],
                "name": customer_tpl[2],
                "surname": customer_tpl[3],
                "patronymic": customer_tpl[4],
                "country": customer_tpl[5],
                "state": customer_tpl[6],
                "city": customer_tpl[7],
                "street": customer_tpl[8],
                "house_number": customer_tpl[9],
                "phone_number": customer_tpl[10],
                "email": customer_tpl[11],
                "debt": customer_tpl[12]
            }
            customers_out.append(category_dict)
        return customers_out


class Customer(Resource):

    # @jwt_required()
    def get(self, ipn):
        customer_tpl = customers.get_customer(ipn)
        json_out = {
            "ipn": customer_tpl[0],
            "notes": customer_tpl[1],
            "name": customer_tpl[2],
            "surname": customer_tpl[3],
            "patronymic": customer_tpl[4],
            "country": customer_tpl[5],
            "state": customer_tpl[6],
            "city": customer_tpl[7],
            "street": customer_tpl[8],
            "house_number": customer_tpl[9],
            "phone_number": customer_tpl[10],
            "email": customer_tpl[11],
            "debt": customer_tpl[12]
        }
        return json_out

    # @jwt_required()
    def post(self):
        try:
            customer_schema = CustomerSchema.parse_raw(json.dumps(request.get_json()))
        except ValidationError:
            return {"message": "invalid arguments"}
        return customers.add_customer(customer_schema.ipn, customer_schema.name, customer_schema.surname,
                                      customer_schema.patronymic, customer_schema.country, customer_schema.state,
                                      customer_schema.city, customer_schema.street, customer_schema.house_number,
                                      customer_schema.phone_number, customer_schema.email, customer_schema.debt,
                                      customer_schema.notes)

    # @jwt_required()
    def delete(self, ipn):
        return customers.delete_customer(ipn)

