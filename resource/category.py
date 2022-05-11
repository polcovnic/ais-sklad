import json
from typing import Optional

from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from pydantic import BaseModel, ValidationError

from models import categories


class CategoriesSchema(BaseModel):
    name: str
    notes: Optional[str]


class Categories(Resource):
    # @jwt_required()
    def get(self):
        categories_tpl = categories.get_categories()
        categories_out = []
        for category_tpl in categories_tpl:
            category_dict = {
                "id": category_tpl[0],
                "name": category_tpl[1],
                "notes": category_tpl[2]
            }
            categories_out.append(category_dict)
        return categories_out


class Category(Resource):

    # @jwt_required()
    def get(self, _id):
        category_tpl = categories.get_category_by_id(_id)
        json_out = {
            "id": category_tpl[0],
            "name": category_tpl[1],
            "notes": category_tpl[2]
        }
        return json_out

    # @jwt_required()
    def post(self):
        try:
            category_schema = CategoriesSchema.parse_raw(json.dumps(request.get_json()))
        except ValidationError:
            return {"message": "invalid arguments"}
        return categories.add_new_category(category_schema.name, category_schema.notes)

    # @jwt_required()
    def delete(self, _id):
        return categories.delete_category(_id)
