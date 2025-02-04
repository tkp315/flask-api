from src.utils.asyncFunctionHandler import asyncFunctionHandler
from flask import request as req,jsonify
from src.utils.apiError import ApiError
from src.utils.apiResponse import ApiResponse
@asyncFunctionHandler
async def login():
        data = req.get_json()
        email= data['email']
        password= data['password']
        if not data:
         raise ApiError(401,"Data not found")
        #  raise error()
        if(not email or not password):
           raise ApiError(401,"Enter required Fields")
        # print(ApiError(401,"Enter required Fields"))
       
        
        response = ApiResponse("Login", True, "Logged In Successfully", 200, data)
        return response()
    

    
