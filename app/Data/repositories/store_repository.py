from Data.models.models import Store


def store_changes(store):
    store.save()


def find_store(keyword):
    return Store.find(**{'name': keyword})


def remove_store(store):
    Store.remove(**store)


def add_store(store):
    name, street_address, zip_code, city, phone, email = store
    store = Store({'name': name,
                   'street_address': street_address,
                   'zip_code': zip_code,
                   'city': city,
                   'phone': phone,
                   'email': email})
    store.save()
    return store


