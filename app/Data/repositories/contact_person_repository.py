from Data.db import session
from Data.models.contact_persons import ContactPerson


def find_contact_person(cp_id):
    return session.query(ContactPerson).filter(ContactPerson.id.like(f'%{cp_id}%')).all()