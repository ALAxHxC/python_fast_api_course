from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import session, Session
from database_sql.models import Cities
from database_sql.queries.base_queries import BaseQueries
from schemas.cities import CitiesSchema


class CityQueries(BaseQueries):
    def __init__(self):
        super().__init__(Cities, CitiesSchema, Cities.cod_name)

    def add (self,city:CitiesSchema,session:Session):
        try:

            session.add(Cities(**city.dict()))
            session.commit()
            return session.query(Cities).filter(Cities.cod_name==city.cod_name).first()
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=str(e))
    def all (self, session:Session):
        return session.query(Cities).all()



