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
