from Data.db import session
from Data.models.contact_persons import ContactPerson


def add_contact_person(contact_person):
    name, phone, email = contact_person
    contact_person = ContactPerson(name=name, phone=phone, email=email)
    session.add(contact_person)
    session.commit()
    return contact_person
