import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .settings import *


Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

