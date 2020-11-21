import Data.repositories.employee_repository as cr

def find_employee(search):
    matches = cr.find_employee(search)


def add_employee(e):
    cr.add_employee(e)