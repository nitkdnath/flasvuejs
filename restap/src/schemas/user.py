from src.common import db, ma
class UserSchema(ma.Schema):
    class Meta:
        fields = ("id","name", "email", "phone_number","user_address")

user_schema = UserSchema()
users_schema = UserSchema(many=True)
