from flask import jsonify
class ApiResponse:
    def __init__(self,title,success,message,statusCode,data):
        self.title= title
        self.success=success
        self.message= message
        self.statusCode= statusCode
        self.data= data if data is not None else {}
        
    def __call__(self):
        """Converts object into dictionary for JSON """
        
        return jsonify({
            "title":self.title,
            "success":self.success,
            "message":self.message,
            "statusCode":self.statusCode,
            "data":self.data
        })


        