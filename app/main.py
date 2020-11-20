from Data.db import Base, engine

from Data.models.products import Product
from Data.models.carmodels import CarModel
# from Data.models.contactpersons import ContactPerson
# from Data.models.customercar import CustomerCar
# from Data.models.customers import Customer
# from Data.models.customertypes import CustomerType
# from Data.models.employees import Employee
# from Data.models.orders import Order
# from Data.models.partnertypes import PartnerType
# from Data.models.partners import Partner
# from Data.models.stores import Store
# from Data.models.orderedproducts import OrderedProduct
from Data.models.matching_products import matching_products


def main():
    Base.metadata.create_all(engine)
    # contactperson = ContactPerson()
    # customercar = CustomerCar()
    # customers = Customer()
    # customertype = CustomerType()
    # employee = Employee()
    # order = Order()
    # orderedproduct = OrderedProduct()
    # store = Store()


if __name__ == '__main__':
    main()
