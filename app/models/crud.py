from app.models.databases import session
from app.models.modelsUser import User


# function to fetch the user in the database
def get_user(number):
    query = session.query(User).filter(User.number == number).first()
    return query


# function to create user
def create_user(number):
    query = User(number=number)
    session.add(query)
    session.commit()
    # returning created user
    return query


# function to update user
def update_information(number, name=None, unity=None, sector=None, level=None, stage=None, active=None):
    query = session.query(User).filter(User.number == number).first()
    print(name)
    if name:
        query.name = name
    if unity:
        query.unity = unity
    if sector:
        query.sector = unity
    if level:
        query.level = level
    if stage:
        query.stage = stage
    if active:
        query.active = active

    session.add(query)
    session.commit()
    return query

def reset_user(number):
    query = session.query(User).filter(User.number == number).first()
    return query


