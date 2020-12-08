import Data.repositories.customer_car_repository as ccr


def add_customer_car(customer, c):
    added_car = ccr.add_customer_car(customer, c)
    return f"{added_car} - tillagd"


def find_customer_car(customer, regnr):
    return ccr.find_customer_car(customer, regnr)


def remove_customer_car(customer, car):
    ccr.remove_customer_car(customer, car)
    return f"{car} - borttagen"


def remove_all_customer_cars(chosen_customer):
    customer_cars = chosen_customer.customer_cars
    for car in customer_cars:
        ccr.remove_customer_car(car)
