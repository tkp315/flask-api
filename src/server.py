from src.app import app
from config.config import Config
from src.database.db import connect_to_db  # Ensure this is now sync

def start_server():
    try:
        connect_to_db()  # Now a synchronous function
        print("PostgreSQL connected successfully!")
        app.run(debug=Config.DEBUG, port=Config.PORT)

    except Exception as err:
        print("Unable to connect to the database:", err)

if __name__ == "__main__":
    start_server()
