from flask import Blueprint
from flask_restful import Api
from routers.userRouters import UserRouter, LoginRouter, RegisterRouter, LogoutRouter

api_bp = Blueprint('api', __name__)

api = Api(api_bp)

api.add_resource(UserRouter, '/users', '/users/<int:user_id>')
api.add_resource(LoginRouter, '/login')
api.add_resource(LogoutRouter, '/logout')
api.add_resource(RegisterRouter, '/register')
