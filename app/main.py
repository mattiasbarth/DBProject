from db import Base, engine, session
from models.stores import Store
from models.employees import Employee
from models.orderedproducts import Orderered_product
from models.orders import Order


def main():
    Base.metadata.create_all(engine)
    store = Store()
    employee = Employee()
    order = Order()
    ordereredproduct = Orderered_product()

if __name__ == '__main__':
    main()
