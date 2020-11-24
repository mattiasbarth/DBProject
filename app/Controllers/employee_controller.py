import Data.repositories.employee_repository as er


def find_employees(search):
    return er.find_employees(search)


def add_employee(e):
    er.add_employee(e)


def remove_employee(chosen_employee):
    er.remove_employee(chosen_employee)
    print(f"{chosen_employee} är nu borttagen")


def change_value(chosen_employee, value, new_value):
    er.change_value(chosen_employee, value, new_value)
    print(f"Uppdaterad!")

def existing_store(store_id):
    return er.existing_store(store_id)