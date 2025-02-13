from src.models.base import TimeStampedModel
from sqlalchemy import Column,Integer,String,Enum,Text
import enum


class UserRole(enum.Enum):
    ADMIN='admin'
    USER= 'user'
    GUEST='guest'

class User (TimeStampedModel):
    __tablename__="user"

    _id=Column(Integer,primary_key=True,autoincrement=True)
    full_name = Column(String(300),nullable=False)
    email = Column(String(150),nullable=False,unique=True)
    phone_no=Column(String(20),nullable=False,unique=True)
    role = Column(Enum(UserRole, native_enum=False), nullable=False, default=UserRole.USER)
    password= Column(String(255),nullable=False)
    refresh_token = Column(Text,nullable=True)

    def __repr__(self):
        return (f"{self.__class__.__name__}, full name:{self.full_name}")

