from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy import update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from database_sql.connection import Base


class BaseQueries:
    __model__ = None
    __schema__ = None
    __id_property__ = None

    def __init__(self, model: Base, schema, id_property) -> None:
        self.__schema__ = schema
        self.__model__ = model
        self.__id_property__ = id_property

    def create(self, session: Session, entity: BaseModel):
        try:
            session.add(self.__model__(**entity.dict()))
            session.commit()
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=str(e))

    def get_by_id(self, session: Session, id_entity):
        print(id_entity,self.__id_property__ )
        return session.query(self.__model__).filter(self.__id_property__ == id_entity).first()

    def all_data(self, session: Session):
        return session.query(self.__model__).all()

    def delete(self, session: Session, id_entity):
        session.query(self.__model__).filter(self.__id_property__ == id_entity).delete()
        session.commit()

    def update(self, session: Session, data: dict, id_entity):
        update_sql = update(self.__model__) \
            .where(self.__id_property__ == id_entity) \
            .values(**data)
        session.execute(update_sql)
        session.commit()
        return self.get_by_id(session, id_entity)
