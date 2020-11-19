from db import Base
from sqlalchemy import Column, Integer, ForeignKey


class MatchingProduct(Base):
    __tablename__ = "matching_products"

    product_id = Column(Integer, ForeignKey("product.id"), primary_key=True, ondelete="Cascade", onupdate="Cascade")
    car_model_id = Column(Integer, ForeignKey("car_models.id"), primary_key=True, ondelete="Cascade", onupdate="Cascade")
