from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from database_sql.models import TypeFuel
from schemas.type_fuel import TypeFuelSchema


class TypeFuelQueries:
    def add(self,typefuel:TypeFuelSchema,session:Session):
        try:
            session.add(TypeFuel(**typefuel.dict()))
            session.commit()
            return session.query(TypeFuel).filter(TypeFuel.description==typefuel.description).first()
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=str(e))
    def all (sel, session:Session):
        return session.query(TypeFuel).all()
