from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from database_sql.connection import Base


class Vehicle(Base):
    __tablename__ = "vehicle"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(45), unique=True, index=True)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45))
    last_name = Column(String(45))


class Cities(Base):
    __tablename__ = "cities"
    country = Column(String(45))
    cod_name = Column(Integer, primary_key=True, index=True)
    name = Column(String(45))


class Actions(Base):
    __tablename__ = "actions"
    description = Column(String(45), primary_key=True)
    medida = Column(String(1))


# SQL ALCHEMY NO SOPORTA MULTIPLES LLAVES
class Brands(Base):
    __tablename__ = "brands"  # se corrige gramatica
    id_runt = Column(String(45), primary_key=True)
    description = Column(String(45))


class Lines(Base):
    __tablename__ = "lines"  # se corrige gramatica
    name = Column(String(45), primary_key=True)
    #hint
    #id_brand = Column(ForeignKey("brands.id_runt"), nullable=True)


class TypeFuel(Base):
    __tablename__ = "type_fuel"  # se corrige gramatica
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(45))
