from sqlalchemy import Column, Integer, String

from database_sql.connection import Base


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
class Cities(Base):
    __tablename__ = "cities"
    country= Column(String(45))
    cod_name= Column(Integer, primary_key=True, index=True)
    name= Column(String(45))
