from flask import jsonify

class ApiError(Exception):
    def __init__(self, statusCode, message="Something went wrong", errors=None):
        super().__init__(message)
        self.statusCode = statusCode
        self.message = message
        self.errors = errors if errors else []

         

    def __call__(self):
        """Convert error details to a dictionary format."""
        return jsonify({
            "statusCode": self.statusCode,
            "message": self.message,
            "errors": self.errors,
            
        }),self.statusCode
