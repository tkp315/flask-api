from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from urllib.parse import urlparse
from config.config import Config

postgress_url = urlparse(Config.DATABASE_URL)

print(f"name:{postgress_url.username},password:{postgress_url.password},path: {postgress_url.path},host: {postgress_url.hostname}")

# Creating a synchronous engine using psycopg2
engine = create_engine(
    f"postgresql+psycopg2://{postgress_url.username}:{postgress_url.password}@{postgress_url.hostname}{postgress_url.path}",
    echo=True,
    connect_args={"sslmode": "require"}  
)

# Creating a synchronous session factory
SessionLocal = sessionmaker(bind=engine, autoflush=True, expire_on_commit=False)


def connect_to_db():
    """Establish connection with the database"""
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print("PostgreSQL connected successfully!")
    except Exception as err:
        print("Unable to connect to the database:", err)
        return err
