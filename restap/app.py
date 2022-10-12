
from src.services.orders import OrderListResource
from src.services.product import ProductListResource,ProductResource
from src.services.users import UserListResource,UserResource
from src.common.base import api,app
from src.services.auth import SignupResource,LoginResource,LogoutResource,Refresh,Admin
api.add_resource(ProductListResource, '/products', endpoint='products')
api.add_resource(ProductResource, '/product/<int:id>', endpoint='product')
api.add_resource(UserListResource, '/users', endpoint='users')
api.add_resource(UserResource, '/user/<int:id>', endpoint='user')
api.add_resource(SignupResource, '/signup', endpoint='signup')
api.add_resource(LoginResource, '/login', endpoint='login')
api.add_resource(OrderListResource, '/orders', endpoint='orders')
api.add_resource(LogoutResource, '/logout', endpoint='logout')
api.add_resource(Refresh, '/refresh', endpoint='refresh')
api.add_resource(Admin, '/admin', endpoint='admin')
if __name__ == "__main__":
    app.run(debug=True, port=9000)