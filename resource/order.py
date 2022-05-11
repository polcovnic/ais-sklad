import json
from datetime import datetime
from typing import Optional, List

from flask_restful import Resource, request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from pydantic import BaseModel, ValidationError

from models import orders, order_rows


class OrderRow(BaseModel):
    product_id: int
    amount: int
    price: int


class OrderSchema(BaseModel):
    customer_ipn: int
    notes: Optional[str]
    rows: List[OrderRow]


class Orders(Resource):
    # @jwt_required()
    def get(self):
        orders_tpl = orders.get_orders()
        orders_out = []
        for order_tpl in orders_tpl:
            order_rows_out = []
            for order_row in order_rows.get_all_rows_in_order(order_tpl[0]):
                order_row_json = {
                    "sum": order_row[1],
                    "product_id": order_row[2]
                }
                order_rows_out.append(order_row_json)
            order_dict = {
                "id": order_tpl[0],
                "notes": order_tpl[1],
                "date": order_tpl[2],
                "customer_ipn": order_tpl[3],
                "sum": order_tpl[4],
                "rows": order_rows_out
            }
            orders_out.append(order_dict)
        return orders_out


class Order(Resource):

    # @jwt_required()
    def get(self, _id):
        order_tpl = orders.get_order_by_id(_id)
        json_out = {
            "id": order_tpl[0],
            "notes": order_tpl[1],
            "date": order_tpl[2],
            "customer_ipn": order_tpl[3],
            "sum": order_tpl[4]
        }
        return json_out

    # @jwt_required()
    def post(self):
        try:
            order_schema = OrderSchema.parse_raw(json.dumps(request.get_json()))
        except ValidationError:
            return {"message": "invalid arguments"}
        _sum = 0
        for order_row in order_schema.rows:
            _sum += order_row.price
        order_id = orders.add_new_order(order_schema.notes, datetime.now(),
                                        order_schema.customer_ipn, _sum)[0]
        order_row_ids = []
        for order_row in order_schema.rows:
            _id = order_rows.add_new_row(order_id, order_row.product_id, order_row.amount, order_row.price)[0]
            order_row_ids.append(_id)
        return {
            "order_id": order_id,
            "order_row_ids": order_row_ids
        }

    # @jwt_required()
    def delete(self, _id):
        return orders.delete_order(_id)
