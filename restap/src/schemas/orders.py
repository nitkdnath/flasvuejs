from src.common import db, ma
#from src.db import model

class OrderSchema(ma.Schema):
    class Meta:
        fields = ("username", "user_address", "phone_number","price")


order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)