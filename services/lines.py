from sqlalchemy.orm import Session
from database_sql.queries.linesqueris import LinesQueries
from schemas.lines import LinesSchema


class LinesServices:
    query=LinesQueries()
    def add (self, lines:LinesSchema,session:Session):
        return self.query.add(lines,session)
    def all (self, session:Session):
        return self.query.all(session)
