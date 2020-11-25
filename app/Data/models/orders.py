from sqlalchemy.sql import functions
from sqlalchemy.orm import relationship
from ..db import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)  # PRIMARY KEY
    customer_id = Column(Integer, ForeignKey('customers.id', ondelete="Set Null", onupdate="Cascade"))  # FOREIGN KEY --> Customers
    employee_id = Column(Integer, ForeignKey('employees.id', ondelete="Set Null", onupdate="Cascade"))  # FOREIGN KEY --> Employees
    store_id = Column(Integer, ForeignKey('stores.id', ondelete="Set Null", onupdate="Cascade"))  # FOREIGN KEY --> Stores

    date_created = Column(TIMESTAMP, nullable=False, default=functions.current_timestamp)
    status = Column(String(45), nullable=False)
    comment = Column(String(150))

    store = relationship('Store', back_populates='orders')
    employee = relationship('Employee')
    customer = relationship('Customer', back_populates='orders')
    products = relationship('Product', secondary='ordered_products')

    def __repr__(self):
        pass
