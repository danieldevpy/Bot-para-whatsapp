import threading
from app.models import crud
import requests


# Class to perform data manipulation
class Account:
    # none attributes, not to be mandatory when booting
    def __init__(self, number: str):
        self.number = number
        self.name = None
        self.unity = None
        self.sector = None
        self.level = None
        self.menu = None
        self.stage = None
        self.message = None
        self.active = None

    def create_user(self):
        user = crud.create_user(number=self.number)
        self.name = user.name
        self.unity = user.unity
        self.sector = user.sector
        self.level = user.level
        self.menu = user.menu
        self.stage = user.stage
        self.message = user.message
        self.active = user.active

    def get_user(self):
        user = crud.get_user(number=self.number)
        if user is not None:
            self.name = user.name
            self.unity = user.unity
            self.sector = user.sector
            self.level = user.level
            self.menu = user.menu
            self.stage = user.stage
            self.message = user.message
            self.active = user.active

        return user

    def update_information(self, name=None, unity=None, sector=None, level=None, menu=None,
                           stage=None, message=None, active=None):
        user = crud.update_information(self.number, name, unity, sector, level, menu, stage, message, active)
        self.name = user.name
        self.unity = user.unity
        self.sector = user.sector
        self.level = user.level
        self.menu = user.menu
        self.stage = user.stage
        self.message = user.message
        self.active = user.active

    def reset_user(self):
        crud.update_information(self.number, name=None, unity=None, sector=None,
                                level=0, menu=0, stage=0, message='Null', active=3)

    def finishing(self, message):
        message_group = f'Um novo chamado foi aberto no GLPI, por: [{self.name, self.unity, self.sector, self.number}]'
        crud.alert_group(message_group)
        title = f'Chamado aberto por: {self.name}/{self.unity}/{self.sector}'
        url = f'http://localhost:2000/{title}/{message}'
        open_glpi = lambda: requests.get(url)
        threading.Thread(target=open_glpi).start()
