from sqlalchemy.orm import declarative_base  # getting the alredy made class
from  src.database.db import SessionLocal
from sqlalchemy import Column,DateTime
from datetime import datetime
Model = declarative_base()



class TimeStampedModel(Model):
    __abstract__=True
    created_at = Column(DateTime,default=datetime.utcnow())
    updated_at = Column(DateTime,default=datetime.utcnow())

