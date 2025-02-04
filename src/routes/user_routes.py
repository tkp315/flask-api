from flask import Blueprint
from src.controllers.user_controller import login

user_routes = Blueprint('user_routes',__name__)


user_routes.route('/login',methods=['POST'])(login)