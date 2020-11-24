from Data.models.employees import Employee
from Data.models.stores import Store
from Data.db import session


def find_employees(search):
    return session.query(Employee).filter(Employee.name.like(f'%{search}%')).all()


def add_employee(e):
    store_id, name, phone, email, job_title = e
    new_employee = Employee(store_id=store_id, name=name, phone=phone, email=email, job_title=job_title)
    session.add(new_employee)
    session.commit()
    print("Ny anställd tillagd")


def remove_employee(chosen_employee):
    session.delete(chosen_employee)
    session.commit()


def change_value(chosen_employee, value, new_value):
    if value == chosen_employee.name:
        chosen_employee.name = new_value
    elif value == chosen_employee.email:
        chosen_employee.email = new_value
    elif value == chosen_employee.phone:
        chosen_employee.phone = new_value
    elif value == chosen_employee.job_title:
        chosen_employee.job_title = new_value
    elif value == chosen_employee.store:
        pass
    session.commit()


def existing_store(store_id):
    return session.query(Store).filter(Store.id.like(f'%{store_id}%')).all()