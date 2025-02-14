from flask import Blueprint
from src.controllers.user_controller import login
from src.controllers.user_controller import sign_in
from flask_jwt_extended import jwt_required
from src.controllers.user_controller import logout
from src.utils.apiResponse import ApiResponse
user_routes = Blueprint('user_routes',__name__)


user_routes.route('/login',methods=['POST'])(login)
user_routes.route('/signup',methods=['POST'])(sign_in)


@user_routes.route('/logout', methods=['POST'])
@jwt_required()
def handle_logout():
  logout_result= logout()
  print(logout_result)
  response= ApiResponse("Logout",True,"successfully logged out",200,None)
  return response()