from sqlalchemy import Column, String, Integer, Float
from app.models.databases import Base, engine


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    message = Column(String)

    def __repr__(self):
        return f'{self.message}'


# Class models responsible for creating the table in the database
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    number = Column(String)
    name = Column(String, nullable=True)
    unity = Column(String, nullable=True)
    sector = Column(String, nullable=True)
    level = Column(Integer, default=0)
    menu = Column(Integer, default=0)
    stage = Column(Float, default=0)
    message = Column(String, nullable=True)
    active = Column(Integer, default=0)
    login = Column(String, nullable=True)


Base.metadata.create_all(engine)