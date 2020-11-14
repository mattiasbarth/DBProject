from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..db import Base, engine, session


class Partner(Base):
    """Represent a manufacturer or supplier of car parts."""

    __tablename__ = "partners"

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    street_address = Column(String(100), nullable=False)
    postal_code = Column(String(10), nullable=False)
    city = Column(String(45), nullable=False)
    phone = Column(String(45), nullable=False)
    email = Column(String(100), nullable=True)  # Todo: Use explicit or implicit nullability?
    contact_person_id = Column(Integer, ForeignKey('contact_persons.id'))
    contact_person = relationship('ContactPerson', backref='partners')
    partner_type_id = Column(Integer, ForeignKey('partner_types.id'))
    type = relationship('PartnerType', backref='partners')
