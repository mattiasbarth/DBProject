
import Data.repositories.employee_repository as cr


def save_changes(chosen_customer):
    cr.save_changes(chosen_customer)

    
def find_customer_by_name(keyword):
    return cr.find_customer_by_name(keyword)


def find_customer_by_id(keyword):
    return cr.find_customer_by_id(keyword)


def find_customer_by_phone(keyword):
    return cr.find_customer_by_phone(keyword)

