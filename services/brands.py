from sqlalchemy.orm import Session
from database_sql.queries.brandsqueries import BrandsQueries
from schemas.brands import BrandsSchema


class BrandsServices:
    query = BrandsQueries()

    def add(self, brands: BrandsSchema, session: Session):
        return self.query.add(brands, session)

    def all(self, session: Session):
        return self.query.all(session)


    '''
    hint
    def get_by_id_runt(self, session, id_runt):
        return self.query.get_by_runt(session, id_runt)
    '''