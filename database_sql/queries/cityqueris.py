from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import session, Session
from database_sql.models import Cities
from schemas.cities import CitiesSchema


class CityeQueries:
    def add (self,city:CitiesSchema,session:Session):
        try:

            session.add(Cities(**city.dict()))
            session.commit()
            return session.query(Cities).filter(Cities.cod_name==city.cod_name).first()
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=str(e))
    def all (sel, session:Session):
        return session.query(Cities).all()



