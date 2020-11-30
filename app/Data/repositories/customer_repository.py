from Data.db import session
from Data.models.customers import Customer


def save_changes(_):
    session.commit()
    
    
def find_customer_by_name(keyword):
    return session.query(Customer).filter(Customer.name.like(f'%{keyword}%')).all()


def find_customer_by_id(keyword):
    return session.query(Customer).filter(Customer.id == keyword).all()


def find_customer_by_phone(keyword):
    return session.query(Customer).filter(Customer.phone.like(f'%{keyword}%')).all()


def remove_customer(chosen_customer):
    session.delete(chosen_customer)
    session.commit()