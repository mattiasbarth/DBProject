from Data.models import Document, db


class Customer(Document):
    collection = db.customers


class Employee(Document):
    collection = db.employees


class Store(Document):
    collection = db.stores


class Order(Document):
    collection = db.orders


class Product(Document):
    collection = db.products


class Partner(Document):
    collection = db.partners

