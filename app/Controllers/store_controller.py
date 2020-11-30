import Data.repositories.store_repository as sr
from Data.models.stores import Store


def store_changes(store):
    sr.store_changes()
    return f"Butiken {store} har uppdaterats."


def find_store(keyword):
    return sr.find_store(keyword)


def remove_store(store):
    sr.remove_store(store)
    return f"Butiken {store} har tagits bort."


def add_store(store_data):
    name, street_address, zip_code, city, phone, email = store_data
    store = Store(name=name, street_address=street_address, zip_code=zip_code, city=city, phone=phone, email=email)
    sr.add_store(store)
    return f"Butiken {store} har lagts till."


def main():
    pass


if __name__ == "__main__":
    main()
