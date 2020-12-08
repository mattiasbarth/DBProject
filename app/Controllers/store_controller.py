import Data.repositories.store_repository as sr


def store_changes(store):
    sr.store_changes()
    return f"Butiken {store} har uppdaterats."


def find_store(keyword):
    return sr.find_store(keyword)


def find_store_by_id(keyword):
    return sr.find_store_by_id(keyword)


def remove_store(store):
    sr.remove_store(store)
    return f"Butiken {store} har tagits bort."


def add_store(store):
    sr.add_store(store)
    return f"Butiken {store.name} har lagts till."


def main():
    pass


if __name__ == "__main__":
    main()
