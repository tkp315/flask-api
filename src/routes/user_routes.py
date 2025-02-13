from flask import Blueprint
from src.controllers.user_controller import login
from src.controllers.user_controller import sign_in


user_routes = Blueprint('user_routes',__name__)


user_routes.route('/login',methods=['POST'])(login)
user_routes.route('/signup',methods=['POST'])(sign_in)