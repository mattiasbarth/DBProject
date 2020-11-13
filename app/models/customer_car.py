from ..db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class CustomerCar(Base):
    __tablename__ = "customer_cars"

    regnr = Column(String(10), primary_key=True, autoincrement=False)
    car_model_id = Column(Integer, ForeignKey("car_models.id"), nullable=False)
    customer_id = Column(Integer, ForeignKey("customer.id"), nullable=False)
    color = Column(String(15), nullable=False)
    car_model = relationship("Car_model")
    customer = relationship("Customer", back_populates="CustomerCar")

    def __repr__(self):
        return f"Bilen med registreringsnummer {self.regnr} ägs av kund {self.customer}."
