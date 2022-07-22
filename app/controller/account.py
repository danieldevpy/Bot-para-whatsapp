from app.models import crud


# Class to perform data manipulation
class Account:
    # none attributes, not to be mandatory when booting
    def __init__(self, number: str, name=None, unity=None, sector=None, level=None, stage=None, active=None):
        self.number = number
        self.name = name
        self.unity = unity
        self.sector = sector
        self.level = level
        self.stage = stage
        self.active = active

    def get_user(self):
        user = crud.get_user(number=self.number)
        if user is not None:
            self.name = user.name
            self.unity = user.unity
            self.sector = user.sector
            self.level = user.level
            self.stage = user.stage
            self.active = user.active
        return user

    def create_user(self):
        user = crud.create_user(number=self.number)
        self.name = user.name
        self.unity = user.unity
        self.sector = user.sector
        self.level = user.level
        self.stage = user.stage
        self.active = user.active

    def update_information(self, name=None, unity=None, sector=None, level=None, stage=None, active=None):
        user = crud.update_information(self.number, name, unity, sector, level, stage, active)
        self.name = user.name
        self.unity = user.unity
        self.sector = user.sector
        self.level = user.level
        self.stage = user.stage
        self.active = user.active
