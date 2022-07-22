from sqlalchemy import Column, String, Integer, Float
from app.models.databases import Base, engine


# Class models responsible for creating the table in the database
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    number = Column(String)
    name = Column(String, nullable=True)
    unity = Column(String, nullable=True)
    sector = Column(String, nullable=True)
    level = Column(Integer, default=0)
    stage = Column(Float, default=0)
    active = Column(Integer, default=0)


Base.metadata.create_all(engine)
