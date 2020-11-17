from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..db import Base


class Customer(Base):

    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    customer_type_id = Column(
        Integer,
        ForeignKey('customertypes.id', ondelete="Cascade", onupdate="Restrict"),
        nullable=False)  # Foreign Key --> CustomerTypes
    contact_id = Column(
        Integer,
        ForeignKey('contactpersons.id', ondelete="Set Null", onupdate="Cascade")
        )  # Foreign Key --> ContactPersons
    name = Column(String(100), nullable=False)
    street_address = Column(String(45), nullable=False)
    postal_code = Column(String(10), nullable=False)
    city = Column(String(45), nullable=False)
    phone = Column(String(25), nullable=False)
    email = Column(String(100), nullable=False)

    orders = relationship('Order', back_populates='customers')
    customercars = relationship('CustomerCar', back_populates='customers')
    contactpersons = relationship('ContactPerson', back_populates='customers')
    customertypes = relationship('CustomerType', back_populates='customers')  # Todo: Use singular customertypes?

    def __repr__(self):
        pass
