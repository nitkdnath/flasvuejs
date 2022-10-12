from src.schemas.user import users_schema,user_schema
from flask_restful import Resource,request
from src.db.model import db, User
class UserListResource(Resource):
    def get(self):
        user = User.query.all()
        return users_schema.dump(user)

    def post(self):
        new_User = User(
            name=request.json['name'],
            email=request.json['email'],
            phone_number=request.json['phone_number'],
            password=request.json['password']


        )
        db.session.add(new_User)
        db.session.commit()
        return user_schema.dump(new_User)

class UserResource(Resource):
    def get(self, id):
        user_select = User.query.get_or_404(id)
        return user_schema.dump(user_select)

    def put(self,id):
        user_update = User.query.get_or_404(id)

        _name = request.json['name'],
        _email = request.json['email'],
        _phone_number = request.json['phone_number'],
        _password = request.json['password']
        user_update.name = _name
        user_update.email = _email
        user_update.phone_number = _phone_number
        user_update.password = _password
        db.session.add( user_update)
        db.session.commit()
        return user_schema.dump(user_update)


    def patch(self, id):
        User = User.query.get_or_404(id)

        if 'User_name' in request.json:
            User.name = request.json['User_name']
        if 'User_rate' in request.json:
            User.content = request.json['User_rate']
        if 'quantity' in request.json:
            User.content = request.json['quantity']


        db.session.commit()
        return user_schema.dump(User)

    def delete(self, id):
        User = User.query.get_or_404(id)
        db.session.delete(User)
        db.session.commit()
        return '', 204
