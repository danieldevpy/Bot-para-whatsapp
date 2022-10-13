from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Database creation
engine = create_engine('sqlite:///app/models/db/banco.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


