from src.utils.asyncFunctionHandler import asyncFunctionHandler
from flask import request as req,jsonify,make_response as res
from src.utils.apiError import ApiError
from src.utils.apiResponse import ApiResponse
from src.models.user import User
from src.database.db import SessionLocal 
from src.database.db import session,engine
import bcrypt
from sqlalchemy import text, inspect, or_
from src.models.user import UserRole
from flask_jwt_extended import (
    create_access_token,create_refresh_token,jwt_required,get_jwt_identity,
)
from src.app import jwt

import datetime

@asyncFunctionHandler
async def sign_in():
    userData = req.get_json()
    full_name=userData['full_name']
    email = userData['email']
    phone_no= userData['phone_no']
   #  role = userData.get('role','user')
    password = userData['password']
    confirmPassword = userData['confirmPassword']
    dataArray=[full_name,email,phone_no,password,confirmPassword]
    session = SessionLocal()
    for x in dataArray:
        if(not x):
            raise ApiError(401,"Required fields are necessary")

    isAlreadyUser = session.query(User).filter(
        (User.email==email)| (User.phone_no==phone_no)
      ).first()
    if(isAlreadyUser):
        raise ApiError(401,"User is already present, please login ")
   
    if(password!=confirmPassword):
        raise ApiError(401,"Password Not matched")
    encrypted_password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt(10)).decode("utf-8")
    new_user = User(
        full_name=full_name,
        phone_no=phone_no,
        email=email,
        password=encrypted_password,
        role=UserRole.ADMIN
    )
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    response = ApiResponse("Sign Up", True, "User Registered Successfully", 201, {"user_id": new_user._id})
    return response()


@asyncFunctionHandler
async def login():
    login_data = req.get_json();
    print(login_data)
    credential= login_data['credential']
    password = login_data['password']
    # is user found
    user = session.query(User).filter(
        or_(User.email==credential , User.phone_no==credential)
    ).first()
    
    
    if(not user):
        raise ApiError(404,"User Not Found")
    
    # inspector = inspect(engine)
    # tables = inspector.get_table_names()

    # is password correct
    
    isPasswordCorrect = bcrypt.checkpw(password.encode('utf-8'),(user.password).encode('utf-8'))
    if(not isPasswordCorrect):
        raise ApiError(401,"INCORECT PASSWORD")
    

    # generate the tokens

    access_token = create_access_token(identity={"email":credential,"_id":user._id})
    refresh_token = create_refresh_token(identity={"email":credential,"_id":user._id})

    user.refresh_token= refresh_token
    session.commit()

   
    userDetails = {
       "_id":user._id,
       "email":user.email,
       "full_name":user.full_name,
       "phone_no":user.phone_no,
       "role":user.role.value
   }
    

    # return res
    response = res( ApiResponse("Sign Up", True, "User Registered Successfully", 201, {"user":userDetails})())
    response.set_cookie("access_token",access_token,httponly=True)
    response.set_cookie("refresh_token",access_token,httponly=True)

    return response