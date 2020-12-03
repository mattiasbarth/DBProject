from Data.models.models import Customer


def save_changes(customer):
    customer.save()
    
    
def find_customer_by_name(keyword):
    return Customer.find(**{'name': keyword})


def find_customer_by_id(keyword):
    return Customer.find(**{'_id': keyword})


def find_customer_by_phone(keyword):
    return Customer.find(**{'phone': keyword})


def add_business(customer):
    name, street_address, zip_code, city, phone, email, customer_type, contact_id = customer
    customer = Customer({'name': name,
                         'street_address': street_address,
                         'zip_code': zip_code,
                         'city': city,
                         'phone': phone,
                         'email': email,
                         'customer_type_id': customer_type,
                         'contact_id': contact_id})
    customer.save()
    return customer


def add_private(customer):
    name, street_address, zip_code, city, phone, email, customer_type = customer
    customer = Customer({'name': name,
                         'street_address': street_address,
                         'zip_code': zip_code,
                         'city': city,
                         'phone': phone,
                         'email': email,
                         'customer_type_id': customer_type})
    customer.save()
    return customer


def remove_customer(customer):
    Customer.remove(**customer)


