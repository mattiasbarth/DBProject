from Data.db import session
from Data.models.stores import Store


def search_store(keyword):
    return session.query(Store).filter(Store.name.like(f'%{keyword}%')).all()


def main():
    keyword = "buf"
    store = session.query(Store).filter(Store.name.like(f'%{keyword}%')).all()
    print(store)


if __name__ == '__main__':
    main()
