from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..db import Base


class Partner(Base):

    __tablename__ = "partners"

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    street_address = Column(String(100), nullable=False)
    postal_code = Column(String(10), nullable=False)
    city = Column(String(45), nullable=False)
    phone = Column(String(45), nullable=False)
    email = Column(String(100), nullable=True)  # Todo: Use explicit or implicit nullability?
    contact_person_id = Column(Integer, ForeignKey('contactpersons.id'), ondelete='Set Null', onupdate='Cascade')
    contact_person = relationship('ContactPerson', backref='partners')
    partner_type_id = Column(Integer, ForeignKey('partnertypes.id'), ondelete='Restrict', onupdate='Cascade')
    type = relationship('PartnerType', backref='partners')

    partnertypes = relationship('PartnerType', back_populates='partners')
    contactpersons = relationship('ContactPerson', back_populates='partners')
    products = relationship('Product', back_populates='partners')

    def __repr__(self):
        pass
