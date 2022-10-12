from logging import NullHandler
from flask_sqlalchemy import Model
from sqlalchemy.ext.declarative import declarative_base
from src.common.base import db

orderitems = db.Table('orderitems',db.Model.metadata,
                     db.Column('order_id',db.Integer, db.ForeignKey('orders.id'),primary_key=True),
                     db.Column('product_id',db.Integer, db.ForeignKey('products.id'),primary_key=True),
                     db.Column('quantity',db.Integer))

class OrderItems(db.Model):
        orderId = db.Column('order_id', db.Integer, db.ForeignKey('orders.id'), primary_key=True)
        productId = db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True)
        quantity = db.Column('quantity', db.Integer, nullable=False)
        email = db.Column(db.String(120), index=True)
        order = db.relationship('Orders', back_populates='orderitems')
        product = db.relationship('Product', back_populates='orderitems')

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), index=True, unique=True)
    phone_number = db.Column(db.Integer, index=True,)
    password = db.Column(db.BLOB, nullable=False)
    user_address = db.Column(db.String(250), nullable=False)
    role = db.Column(db.Integer, index=True, default=0)
    created = db.Column(db.DateTime(timezone=True), default=db.func.current_timestamp(), nullable=False)
    order = db.relationship("Orders", backref='users',lazy = True)
    def __repr__(self):
        return '<User %s>' % self.name
class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    product_name = db.Column(db.String(50))
    product_rate = db.Column(db.Float(precision=2))
    image = db.Column(db.String(60))
    quantity = db.Column(db.Integer,nullable=False)
   # order = db.relationship("OrderItems", back_populates="xyz")
    orderitems = db.relationship('OrderItems', back_populates='product', lazy=True)

    def __repr__(self):
        return '<Product %s>' % self.product_name


class Orders(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    username = db.Column(db.String(255))
    user_address = db.Column(db.String(250))
    price = db.Column(db.Float(20))
    quantity = db.Column(db.Integer, default=1)
    created = db.Column(db.DateTime(timezone=True), default=db.func.current_timestamp(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    #orderip = db.relationship("Product", backref=db.backref("orderproduct", lazy=True))
    orderitems = db.relationship('OrderItems', back_populates="order", lazy=True)
    #prod = db.relationship("OrderItems", back_populates="orders")

    def __repr__(self):
        return '<Orders %s>' % self.name

