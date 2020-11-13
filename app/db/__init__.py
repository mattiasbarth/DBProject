import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('sqlite:///projekt.sqlite')

Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

