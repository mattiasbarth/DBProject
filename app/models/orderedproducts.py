from db import Base
from sqlalchemy import Column, Integer, ForeignKey


class OrderedProduct(Base):
    __tablename__ = 'ordered_products'

    order_id = Column(Integer, ForeignKey('orders.id'), primary_key=True, ondelete="Cascade", onupdate="Cascade")
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True, ondelete="Restrict", onupdate="Cascade")
    product_amount = Column(Integer, nullable=False)

    def __repr__(self):
        pass
