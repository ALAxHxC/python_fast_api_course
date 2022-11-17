from fastapi import HTTPException
from sqlalchemy.orm import Session
from database_sql.queries.linesqueris import LinesQueries
from schemas.lines import LinesSchema
from services.brands import BrandsServices


class LinesServices:
    query = LinesQueries()
    brand_services = BrandsServices()

    def add(self, lines: LinesSchema, session: Session):
        return self.query.add(lines, session)

    def all(self, session: Session):
        return self.query.all(session)
#HINT
#brand = self.brand_services.get_by_id_runt(session, lines.id_brand)
#        if brand is None:
#            raise HTTPException(status_code=404, detail="Brand not found")