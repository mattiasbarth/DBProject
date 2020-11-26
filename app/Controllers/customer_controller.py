import Data.repositories.customer_repository as cr


def find_customer_by_name(keyword):
    return cr.find_customer_by_name(keyword)


def find_customer_by_id(keyword):
    return cr.find_customer_by_id(keyword)


def find_customer_by_phone(keyword):
    return cr.find_customer_by_phone(keyword)
