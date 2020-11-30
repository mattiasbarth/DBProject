import Data.repositories.customer_repository as cr


def save_changes(chosen_customer):
    cr.save_changes(chosen_customer)
    return "Uppdaterad"

    
def find_customer_by_name(keyword):
    return cr.find_customer_by_name(keyword)


def find_customer_by_id(keyword):
    return cr.find_customer_by_id(keyword)


def find_customer_by_phone(keyword):
    return cr.find_customer_by_phone(keyword)


def remove_customer(chosen_customer):
    cr.remove_customer(chosen_customer)
    return f"{chosen_customer} - borttagen"