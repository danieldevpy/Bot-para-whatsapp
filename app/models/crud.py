from app.models.databases import session
from app.models.modelsUser import User, Group


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
def update_information(number, name, unity, sector, level, menu, stage, message, active):
    query = session.query(User).filter(User.number == number).first()
    if name is not None:
        query.name = name
    if unity is not None:
        query.unity = unity
    if sector is not None:
        query.sector = sector
    if level is not None:
        query.level = level
    if menu is not None:
        query.menu = menu
    if stage is not None:
        query.stage = stage
    if message is not None:
        query.message = message
    if active is not None:
        query.active = active

    session.add(query)
    session.commit()
    return query


def alert_group(message):
    query = Group(message=message)
    session.add(query)
    session.commit()


def get_group():
    query = session.query(Group).first()
    session.delete(query)
    session.commit()
    return query
