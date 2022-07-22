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

    if name:
        query.name = name
    if unity:
        query.unity = unity
    if sector:
        query.sector = sector
    if level:
        query.level = level
    if menu:
        query.menu = menu
    if stage:
        query.stage = stage
    if message:
        query.message = message
    if active:
        query.active = active

    session.add(query)
    session.commit()
    return query


def alert_group(message):
    pass