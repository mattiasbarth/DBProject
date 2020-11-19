from Data.db import Base, engine
from Data.models.stores import Store
from Data.models.employees import Employee
from Data.models.orderedproducts import Orderered_product
from Data.models.orders import Order


def main():
    Base.metadata.create_all(engine)
    store = Store()
    employee = Employee()
    order = Order()
    ordereredproduct = Orderered_product()


if __name__ == '__main__':
    main()
