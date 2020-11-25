from Data.db import session
from Data.models.stores import Store


def store_changes():
    session.commit()


def find_store(keyword):
    return session.query(Store).filter(Store.name.like(f'%{keyword}%')).all()


def remove_store(store):
    session.delete(store)


def add_store(store):
    session.add(store)
    session.commit()

