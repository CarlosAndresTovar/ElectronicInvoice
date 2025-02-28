from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from db import engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String,nullable=False)
    email = Column(String, nullable=False)
    nit = Column(String, nullable=False)

Base.metadata.create_all(engine)