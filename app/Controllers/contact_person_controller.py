import Data.repositories.contact_person_repository as cpr

def find_contact_person(cp_id):
    contactperson = cpr.find_contact_person(cp_id)
    if len(contactperson) == 0:
        return False
    else:
        return True
