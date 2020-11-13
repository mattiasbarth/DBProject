from ..db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, types
from sqlalchemy.orm import relationship
import sqlalchemy


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    description = Column(String(150), nullable=False)
    inventory_id = Column(String(15), nullable=False)
    stock = Column(Integer, nullable=False)
    price_in = Column(Integer, nullable=False)
    price_out = Column(Integer, nullable=False)
    lowest_amount = Column(Integer, nullable=False)
    automatic_order_number = Column(Integer, nullable=False)
    expected_delivery_date = Column(types.Date)
    manufacturer_id = Column(Integer, ForeignKey("partners.id"), nullable=False)
    supplier_id = Column(Integer, ForeignKey("partners.id"), nullable=False)

    manufacturer = relationship("Partners")
    supplier = relationship("Partners")


    def __repr__(self):
        return f"{self.name} - {self.description}. Lagerplats: {self.inventory_id}. Lagerantal: {self.stock}. Inpris: "\
               f"{self.price_in}, utpris: {self.price_out}. Tillverkare: {self.manufacturer}. Leverantör: {self.supplier}"
