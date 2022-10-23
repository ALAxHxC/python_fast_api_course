from sqlalchemy.orm import Session

from database_sql.queries.city import CityQueries
from schemas.city import CitySchema


class CityServices:
    city_queries = CityQueries()

    def add(self, city: CitySchema, session: Session):
        return self.city_queries.add(city, session)

    def all(self, session: Session):
        return self.city_queries.all(session)

    def remove(self, id,session: Session):
        return self.city_queries.remove(id, session)