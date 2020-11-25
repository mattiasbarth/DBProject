import Data.repositories.employee_repository as er


def find_employees(search):
    return er.find_employees(search)


def add_employee(e):
    er.add_employee(e)
    return f"{e.name} tillagd"


def remove_employee(chosen_employee):
    er.remove_employee(chosen_employee)
    return f"{chosen_employee} är nu borttagen"


def save_changes(chosen_employee):
    er.save_changes(chosen_employee)
    return "Uppdaterad!"


def existing_store(store_id):
    return er.existing_store(store_id)