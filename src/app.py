from flask import Flask
from config.config import Config
from flask_cors import CORS
from src.routes.user_routes import user_routes
from src.utils.apiError import ApiError
app = Flask(__name__)


app.config.from_object(Config)
CORS(app,origins=Config.FRONTEND_URL)

app.register_blueprint(user_routes,url_prefix='/api/v1/user')

@app.errorhandler(ApiError)
def handle_api_error(error):
    """Handle custom ApiError and return proper response"""
    return error()
