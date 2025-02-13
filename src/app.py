from flask import Flask
from config.config import Config
from flask_cors import CORS

from flask_jwt_extended import JWTManager
import datetime
app = Flask(__name__)


app.config.from_object(Config)


CORS(app,origins=Config.FRONTEND_URL)


app.config["JWT_SECRET_KEY"] =Config.JWT_SECRET_KEY
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(minutes=int(Config.JWT_ACCESS_TOKEN_EXPIRES))
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = datetime.timedelta(days=int(Config.JWT_REFRESH_TOKEN_EXPIRES))

jwt = JWTManager(app)

from src.routes.user_routes import user_routes
from src.utils.apiError import ApiError
from sqlalchemy import text
from src.database.db import engine  
app.register_blueprint(user_routes,url_prefix='/api/v1/user')

@app.errorhandler(ApiError)
def handle_api_error(error):
    """Handle custom ApiError and return proper response"""
    return error()


def check_active_database():
    """Check current connected database"""
    with engine.connect() as conn:
        result = conn.execute(text("SELECT current_database();"))
        print(" Connected to Database:", result.scalar())

check_active_database()