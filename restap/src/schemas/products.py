from src.common.base import ma
from marshmallow_sqlalchemy import *
import pymysql




class ProductSchema(ma.Schema):
    class Meta:
        fields = ("id","product_name", "product_rate", "quantity","image")


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
