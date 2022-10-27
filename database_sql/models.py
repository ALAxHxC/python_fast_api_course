from sqlalchemy import Column, Integer, String

from database_sql.connection import Base


class City(Base):
    __tablename__ = "city"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(45))
    country = Column(String(45))

class Vehicle(Base):
    __tablename__ = "vehicle"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(45), unique=True, index=True)
    brand = Column(String(45))

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45))
    last_name = Column(String(45))

class Action(Base):
    __tablename__ = "users"
    name = Column(String(45), primary_key=True)
    last_name = Column(String(45))