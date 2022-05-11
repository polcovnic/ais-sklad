import json

from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from pydantic import BaseModel, ValidationError

from models import producers


class ProducerSchema(BaseModel):
    edrpou: int
    name: str
    notes: str
    email: str
    phone_number: str
    country: str
    state: str
    city: str
    street: str
    house_number: int


class Producers(Resource):
    # @jwt_required()
    def get(self):
        producers_tpl = producers.get_producers()
        producers_out = []
        for producer_tpl in producers_tpl:
            producer_dict = {
                "edrpou": producer_tpl[0],
                "name": producer_tpl[1],
                "notes": producer_tpl[2],
                "email": producer_tpl[3],
                "phone_number": producer_tpl[4],
                "country": producer_tpl[5],
                "state": producer_tpl[6],
                "city": producer_tpl[7],
                "street": producer_tpl[8],
                "house_number": producer_tpl[9]
            }
            producers_out.append(producer_dict)
            return producers_out


class Producer(Resource):

    # @jwt_required()
    def get(self, edrpou):
        producer_tpl = producers.get_producer_by_edrpou(edrpou)
        json_out = {
            "edrpou": producer_tpl[0],
            "name": producer_tpl[1],
            "notes": producer_tpl[2],
            "email": producer_tpl[3],
            "phone_number": producer_tpl[4],
            "country": producer_tpl[5],
            "state": producer_tpl[6],
            "city": producer_tpl[7],
            "street": producer_tpl[8],
            "house_number": producer_tpl[9]
        }
        return json_out

    # @jwt_required()
    def post(self):
        try:
            producer_schema = ProducerSchema.parse_raw(json.dumps(request.get_json()))
        except ValidationError:
            return {"message": "invalid arguments"}
        return producers.add_new_producer(producer_schema.edrpou, producer_schema.name, producer_schema.notes,
                                          producer_schema.email, producer_schema.phone_number, producer_schema.country,
                                          producer_schema.state, producer_schema.city, producer_schema.street,
                                          producer_schema.house_number)

    # @jwt_required()
    def delete(self, edrpou):
        return producers.delete_producer(edrpou)
