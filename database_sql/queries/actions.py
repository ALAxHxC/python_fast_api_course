from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import session, Session
from database_sql.models import Actions
from schemas.actions import ActionsSchema


class ActionsQueries:
    def add (self,actions:ActionsSchema,session:Session):
        try:
            session.add(Actions(**actions.dict()))
            session.commit()
            return session.query(Actions).filter(Actions.description==actions.description).first()
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=str(e))
    def all (sel, session:Session):
        return session.query(Actions).all()



