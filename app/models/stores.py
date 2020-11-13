from ..db import Base, engine, session
from sqlalchemy import Column, Integer, String


class Stores(Base):
    __tablename__ = "stores"

    store_id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    street_address = Column(String(100))
    zip_code = Column(String(10))
    city = Column(String(45))
    phone = Column(String(25), nullable=False)
    email = Column(String(100), nullable=False)

    def __repr__(self):
        return f"Butik {self.name} ({self.store_id})"

    def get_address(self):
        return f"Adress: {self.street_address} {self.zip_code} {self.city}"
    
    def get_contact(self):
        return f"Kontaktuppgifter: {self.phone}, {self.email}"



