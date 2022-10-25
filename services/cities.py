from sqlalchemy.orm import Session
from database_sql.queries.cityqueris import CityeQueries
from schemas.cities import CitiesSchema


class CitiesServices:
    query=CityeQueries()
    def add (self, city:CitiesSchema,session:Session):
        return self.query.add(city,session)
    def all (self, session:Session):
        return self.query.all(session)