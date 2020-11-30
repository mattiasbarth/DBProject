import Data.repositories.customer_repository as cr
from Data.models.customers import Customer

def save_changes(chosen_customer):
    cr.save_changes(chosen_customer)
    return "Uppdaterad"


def find_customer_by_name(keyword):
    return cr.find_customer_by_name(keyword)


def find_customer_by_id(keyword):
    return cr.find_customer_by_id(keyword)


def find_customer_by_phone(keyword):
    return cr.find_customer_by_phone(keyword)


def add_business(customer_data):
    name, street_address, zip_code, city, phone, email, customer_type, contact_id = customer_data
    customer = Customer(name=name, street_address=street_address, zip_code=zip_code, city=city, phone=phone,
                        email=email, customer_type_id=customer_type, contact_id=contact_id)
    cr.add_customer(customer)
    return customer, f"{customer} har blivit tillagd som kund."


def add_private(customer_data):
    name, street_address, zip_code, city, phone, email, customer_type = customer_data
    customer = Customer(name=name, street_address=street_address, zip_code=zip_code, city=city, phone=phone,
                        email=email, customer_type_id=customer_type)
    cr.add_customer(customer)
    return customer, f"{customer} har blivit tillagd som kund."

def remove_customer(chosen_customer):
    cr.remove_customer(chosen_customer)
    return f"{chosen_customer} - borttagen"

