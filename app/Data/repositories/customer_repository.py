from Data.db import session
from Data.models.customer_car import CustomerCar
from Data.models.customers import Customer


def save_changes(_):
    session.commit()
    
    
def find_customer_by_name(keyword):
    return session.query(Customer).filter(Customer.name.like(f'%{keyword}%')).all()


def find_customer_by_id(keyword):
    return session.query(Customer).filter(Customer.id == keyword).all()


def find_customer_by_phone(keyword):
    return session.query(Customer).filter(Customer.phone.like(f'%{keyword}%')).all()


def add_car(c):
    customer_id, regnr, car_model_id, color = c
    new_car = CustomerCar(customer_id=customer_id, regnr=regnr, car_model_id=car_model_id, color=color)
    session.add(new_car)
    session.commit()
    return new_car


def find_customer_car(regnr):
    return session.query(CustomerCar).filter(CustomerCar.regnr.like(f'%{regnr}%')).first()


def remove_customer_car(car):
    session.delete(car)
    session.commit()


def remove_customer(chosen_customer):
    customer_cars = chosen_customer.customer_cars
    for car in customer_cars:
        session.delete(car)
    session.delete(chosen_customer)
    session.commit()