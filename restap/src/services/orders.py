#from src.db.addorders import orders_schema, order_schema
from flask_restful import Resource, request


from src.db.model import Orders, Product, User,OrderItems
from src.schemas.orders import orders_schema,order_schema
from src.schemas.products import product_schema,products_schema
from flask import make_response, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_login import login_required
from src.common.base import db
from src.decor.admindec import admin_required
from src.decor.userdec import user_required


class OrderListResource(Resource):

    @jwt_required()
    @admin_required([1])
    def get(self):
        order = Orders.query.all()
        return orders_schema.dump(order)


    @jwt_required()
    @user_required([0])
    def post(self,**kwargs):
        user = get_jwt_identity()
       # _user_address = request.json['user_address']
        _products = request.json['products']
        purchased = {}
        _cart_total = 0
        for _product in _products:
            id = list(_product.values())[0]
            qauntity = list(_product.values())[1]
            _product = Product.query.filter_by(id=id).first()
            _user = User.query.filter_by(email=user).first()
            _user = _user.id
            if _product.quantity < qauntity:
                response = jsonify("Sufficient product Count does not exist")
                return response
            else:
                _cart_total +=(_product.product_rate*qauntity)
                _product.quantity = _product.quantity - qauntity
                db.session.merge(_product)
                db.session.commit()
                purchased.update({id: "added"})
        newoders = Orders(username=get_jwt_identity(),price=_cart_total,user_id = _user)
        db.session.add(newoders)
        db.session.commit()
        user = User.query.filter_by(email=get_jwt_identity()).first()
        with db.session.no_autoflush:
          for _product in _products:
           item = OrderItems()
           item.quantity = _product['quantity']
           item.email = get_jwt_identity()
           #pid = _product['id']
           item.product = Product.query.filter_by(id=_product["id"]).first()
           newoders.orderitems.append(item)
           user.order.append(newoders)
           #newoders.orderip.append(pid)
           db.session.add(user)
           #db.session.add(pid)
           db.session.commit()
        response = jsonify("order added", {"cart total":_cart_total,"purchased products": purchased})
        return response



class OrderResource(Resource):
    @jwt_required()
    @user_required([0])
    def get(self, id):
        order_select = Orders.query.get_or_404(id)
        return order_schema.dump(order_select)

    @jwt_required()
    @admin_required([1])
    def put(self, id):
        order_item = Orders.query.get(id)
        _username = request.json['username']
        _useraddress = request.json['useraddress']
        _products = request.json['products']
        _quantity = request.json['quantity']
        order_item.name = _username
        order_item.rate = _useraddress
        order_item.quantity = _quantity
        db.session.add(order_item)
        db.session.commit()
        # Order = Order_schema.dump(Order_item)
        # return make_response(Order)
        # db.session.commit()
        return order_schema.dump(order_item)

    def patch(self, id):
        orders = Orders.query.get_or_404(id)

        if 'order_name' in request.json:
            orders.name = request.json['Order_name']
        if 'Order_rate' in request.json:
            orders.Order_rate = request.json['Order_rate']
        if 'quantity' in request.json:
            orders.quantity = request.json['quantity']

        db.session.commit()
        return order_schema.dump(Orders)
    @jwt_required()
    @admin_required([1])
    def delete(self, id):
        orders = Orders.query.get_or_404(id)
        db.session.delete(orders)
        db.session.commit()
        return '', 204
