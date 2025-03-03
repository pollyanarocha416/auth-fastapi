from sqlalchemy import Column, Integer, String
from app.db.connection import Base

class UserModel(Base):
    __tablename__ = "users"

    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    username = Column('username', String, nullable=False, unique=True)
    password = Column("password", String, nullable=False)
