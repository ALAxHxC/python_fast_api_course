from fastapi import HTTPException
from sqlalchemy.orm import Session
from database_sql.queries.cityqueris import CityQueries
from schemas.cities import CitiesSchema


class CitiesServices:
    query = CityQueries()

    def add(self, city: CitiesSchema, session: Session):
        return self.query.add(city, session)

    def all(self, session: Session):
        return self.query.all(session)

    def get_by_id(self, session: Session, id_city: int):
        return self.query.get_by_id(session, id_city)

    def get_by_name(self, session: Session, name: str):
        return self.query.get_by_name(session, name)





#HINT TAREA 1:
#        if city.cod_name > 99:
#            raise HTTPException(status_code=404, detail="cod name invalid")