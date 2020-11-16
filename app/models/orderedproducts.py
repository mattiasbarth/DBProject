from sqlalchemy.orm import relationship
from db import Base
from sqlalchemy import Column, Integer, ForeignKey


class Orderered_product(Base):
    __tablename__ = 'ordered_products'

    order_id = Column(Integer, ForeignKey('orders.id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    product_amount = Column(Integer, nullable=False)

    order = relationship('Order', back_populates='ordered_products')
    product = relationship('Product')

    def __repr__(self):
        pass
