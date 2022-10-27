from sqlalchemy.orm import Session
from database_sql.queries.actions import ActionsQueries
from schemas.actions import ActionsSchema


class ActionsServices:
    query=ActionsQueries()
    def add (self, action:ActionsSchema,session:Session):
        return self.query.add(action,session)
    def all (self, session:Session):
        return self.query.all(session)