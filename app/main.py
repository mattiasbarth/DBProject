from Data.db import Base, engine
from UI.main_menu import main_menu
# from Data.models.products import Product
# from Data.models.car_models import CarModel
# from Data.models.contact_persons import ContactPerson
# from Data.models.customer_car import CustomerCar
# from Data.models.customers import Customer
# from Data.models.customer_types import CustomerType
# from Data.models.employees import Employee
# from Data.models.orders import Order
# from Data.models.partner_types import PartnerType
# from Data.models.partners import Partner
# from Data.models.stores import Store
# from Data.models.ordered_products import OrderedProduct
# from Data.models.matching_parts import matching_parts


def main():
    Base.metadata.create_all(engine)
    main_menu()

if __name__ == '__main__':
    main()
