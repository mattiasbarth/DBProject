from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..db import Base, engine, session


class CustomerType(Base):

    __tablename__ = 'customertypes'

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)

    def __repr__(self):
        pass
