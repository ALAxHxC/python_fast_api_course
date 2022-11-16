from sqlalchemy.orm import Session
from database_sql.queries.type_fuelqueris import TypeFuelQueries
from schemas.type_fuel import TypeFuelSchema


class TypeFuelServices:
    query=TypeFuelQueries()
    def add (self, typefuel:TypeFuelSchema,session:Session):
        return self.query.add(typefuel,session)
    def all (self, session:Session):
        return self.query.all(session)
