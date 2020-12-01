from Data.db import session
from Data.models.stores import Store


def store_changes():
    session.commit()


def find_store(keyword):
    return session.query(Store).filter(Store.name.like(f'%{keyword}%')).all()


def remove_store(store):
    session.delete(store)
    session.commit()


def add_store(store_data):
    name, street_address, zip_code, city, phone, email = store_data
    store_data = Store(
        name=name,
        street_address=street_address,
        zip_code=zip_code,
        city=city,
        phone=phone,
        email=email,
    )
    session.add(store_data)
    session.commit()
