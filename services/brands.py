from sqlalchemy.orm import Session
from database_sql.queries.brandsqueries import BrandsQueries
from schemas.brands import BrandsSchema


class BrandsServices:
    query=BrandsQueries()
    def add (self, brands:BrandsSchema,session:Session):
        return self.query.add(brands,session)
    def all (self, session:Session):
        return self.query.all(session)