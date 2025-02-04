import asyncio
from functools import wraps
from flask import jsonify
def asyncFunctionHandler(requestFunction):
     @wraps(requestFunction)  # PRESERVES THE DATA OF ORIGINAL FUNC
     async def wrapper(*args,**kwargs):
          try:
               return await requestFunction(*args,**kwargs)
          except Exception as err:
               status_code=err.code if hasattr(err,"code") and 100<err.code<600 else 500
               return jsonify({
                    "success":False,
                    "message":str(err) or "Internal Server Error"
               }),status_code
     return wrapper
     

