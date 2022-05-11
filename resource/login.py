import json

from flask_restful import Resource, request
from flask_jwt_extended import create_access_token
from pydantic import BaseModel, ValidationError



class LoginSchema(BaseModel):
    cardNumber: str
    pin: str


class Login(Resource):
    def post(self):
        try:
            login_schema: LoginSchema = LoginSchema.parse_raw(json.dumps(request.get_json()))
        except ValidationError:
            return {"message": "invalid arguments"}, 400
        try:
            # bank_id = AccountModel.get_bank_id(login_schema.cardNumber)
            pass
        except AttributeError:
            return {"message": "account does not exist"}, 204
        # bank = BankModel.get_by_id(bank_id)
        # id = bank.start_session(login_schema.cardNumber, login_schema.pin)
        access_token = create_access_token(identity=id)
        return {'access_token': access_token}, 200
