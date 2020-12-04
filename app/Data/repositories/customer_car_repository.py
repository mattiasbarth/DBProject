from Data.models.models import Customer


def add_customer_car(customer, car):  #TODO fungerar ej
    regnr, car_model_id, color = car
    new = {'$customer_cars': {'regnr': regnr, 'color': color}}
    Customer.update(customer, **new)


def find_customer_car(regnr):
    pass


def remove_customer_car(car):
    pass
