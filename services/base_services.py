
from abc import ABC, abstractmethod

from pydantic import BaseModel
from sqlalchemy.orm import Session


class BaseServices(ABC):
    @abstractmethod
    def add(self, session: Session,entity: BaseModel):
        pass

    @abstractmethod
    def search(self,session: Session, limit, skip):
        pass

    @abstractmethod
    def delete(self,session: Session, id_entity):
        pass

    @abstractmethod
    def update(self, session: Session, id_entity, entity: BaseModel):
        pass

    @abstractmethod
    def partial_update(self, session: Session, id_entity, params_to_update: dict):
        pass