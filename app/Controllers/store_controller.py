import Data.repositories.store_repository as sr

def search_store(keyword):
    stores = sr.search_store(keyword)
    return {i+1: store for i, store in enumerate(stores)}

def main():
    pass


if __name__ == "__main__":
    main()
