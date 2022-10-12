import functools

from flask import jsonify, request

from flask_jwt_extended import get_jwt_identity,jwt_required
from src.db.model import User


def admin_required(role_authorized):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            user = get_jwt_identity()

            current_user = User.query.filter_by(email=request.json['email']).first()
            print(current_user.email)
            print(user)
            if current_user.email is not user:
                return current_user.name
            else:
                if current_user.role in role_authorized:
                               kwargs["logged_user"] = current_user
                               return fn(*args, **kwargs)
                else:
                                  return {'message': 'You are not authorized to access this data.'}, 403

        return wrapper

    return decorator