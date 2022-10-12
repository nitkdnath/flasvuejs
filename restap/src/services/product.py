from flask_jwt_extended import jwt_required

from src.schemas.products import products_schema,product_schema
from flask_restful import Resource,request
from src.db.model import db, Product
from flask import make_response

from src.decor.admindec import admin_required


class ProductListResource(Resource):
    def get(self):
        product = Product.query.all()
        return products_schema.dump(product)

    #@jwt_required()
   # @admin_required([1])
    def post(self):
        new_product = Product(
            product_name=request.json['product_name'],
            product_rate=request.json['product_rate'],
            quantity=request.json['quantity'],
            image = request.json

        )
        db.session.add(new_product)
        db.session.commit()
        return product_schema.dump(new_product)

class ProductResource(Resource):
    def get(self, id):
        Product_select = Product.query.get_or_404(id)
        return product_schema.dump(Product_select)

    @jwt_required()
    @admin_required([1])
    def put(self,id):
        Product_item = Product.query.get(id)

        _name = request.json['product_name']

        _rate = request.json['product_rate']

        _quantity = request.json['quantity']


        Product_item.name = _name
        Product_item.rate = _rate
        Product_item.quantity = _quantity
        db.session.add(Product_item)
        db.session.commit()
        #Product = product_schema.dump(Product_item)
        #return make_response(Product)
        #db.session.commit()
        return product_schema.dump(Product_item)

    @jwt_required()
    @admin_required([1])
    def patch(self, id):
        product = Product.query.get_or_404(id)

        if 'product_name' in request.json:
            product.name = request.json['product_name']
        if 'product_rate' in request.json:
            product.product_rate = request.json['product_rate']
        if 'quantity' in request.json:
            product.quantity = request.json['quantity']


        db.session.commit()
        return product_schema.dump(product)

    @jwt_required()
    @admin_required([1])
    def delete(self, id):
        product = Product.query.get_or_404(id)
        db.session.delete(product)
        db.session.commit()
        return '', 204