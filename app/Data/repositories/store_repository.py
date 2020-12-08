from bson import ObjectId
from Data.models.models import Store


def store_changes():
    pass


def find_store(keyword):
    pass


def find_store_by_id(keyword):
    return Store.find(**{'_id': ObjectId(keyword)})


def remove_store(store):
    pass


def add_store(store):
    pass

