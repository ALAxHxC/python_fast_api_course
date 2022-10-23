from typing import List

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from database_sql.models import City
from schemas.city import CitySchema


class CityQueries:
    def add(self, city: CitySchema, session: Session) -> CitySchema:
        try:
            session.add(City(**city.dict()))
            session.commit()
            return session.query(City).filter(City.id == city.id).first()
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail="Integrity error check request")

    def all(self, session: Session) -> List[CitySchema]:
        return session.query(City).all()

    def remove(self, id:int, session: Session):
        session.query(City).filter(City.id == id).delete()
        session.commit()
        return
