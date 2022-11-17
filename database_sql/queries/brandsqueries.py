from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import session, Session
from database_sql.models import Brands
from schemas.brands import BrandsSchema


class BrandsQueries:
    def add(self, brands: BrandsSchema, session: Session):
        try:
            session.add(Brands(**brands.dict()))
            session.commit()
            # AQUI TENIAMOS ESTE ERROR
            # return session.query(brands).filter(brands.description==brands.description).first()
            return session.query(Brands).filter(Brands.description == brands.description).first()
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=str(e))

    def all(sel, session: Session):
        return session.query(Brands).all()
