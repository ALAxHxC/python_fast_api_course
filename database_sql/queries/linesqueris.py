from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from database_sql.models import Lines
from schemas.lines import LinesSchema


class LinesQueries:
    def add(self,lines:LinesSchema,session:Session):
        try:
            session.add(Lines(**lines.dict()))
            session.commit()
            return session.query(Lines).filter(Lines.name==lines.name).first()
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=str(e))
    def all (sel, session:Session):
        return session.query(Lines).all()
