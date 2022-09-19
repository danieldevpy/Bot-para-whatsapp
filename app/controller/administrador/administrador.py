import json

from selenium.webdriver.common.keys import Keys
from app.controller.account import Account
from app.controller.administrador import adm_answers


class Adm:
    def __init__(self, user, text_field, message, same_line):
        self.user = user
        self.text_field = text_field
        self.message = message
        self.same_line = same_line

        if self.user.menu == 0:
            if self.message == '1':
                menu_1 = adm_answers.menu_1
                self.responder(menu_1)
                self.user.update_information(menu=1)
            elif self.message == '2':
                menu_2 = adm_answers.menu_2
                self.responder(menu_2)
                self.user.update_information(menu=2)
        elif self.user.menu == 1:
            if self.user.stage == 0.0:
                infos = self.message
                awnser = None
                number = None
                name = None
                unity = None
                sector = None
                level = None
                menu = None
                stage = None
                active = None
                try:
                    awnser = json.loads(infos)
                    for chave in awnser:
                        if chave == 'number':
                            number = awnser[chave]
                        elif chave == 'name':
                            name = awnser[chave]
                        elif chave == 'unity':
                            unity = awnser[chave]
                        elif chave == 'sector':
                            sector = awnser[chave]
                        elif chave == 'level':
                            level = awnser[chave]
                        elif chave == 'menu':
                            menu = awnser[chave]
                        elif chave == 'stage':
                            stage = awnser[chave]
                        elif chave == 'active':
                            active = awnser[chave]

                    user_edition = Account(number).get_user()
                    if user_edition:
                        user_edition.update_information(name=name, unity=unity, sector=sector, level=level, menu=menu,
                                                        stage=stage, active=active)
                        awnser = adm_answers.detail
                    else:
                        awnser = 'Número não identificado, corrija por favor!'
                except:
                    awnser = 'Verifique se os dados foram digitados corretamente!'

                self.responder(awnser)
                self.user.update_information(menu=9)
        elif self.user.menu == 2:
            user = Account(self.message)
            user.update_information(active=777)
            detail = adm_answers.detail
            self.responder(detail)
            self.user.update_information(menu=9)
        elif self.user.menu == 9:
            if self.message == '1':
                menu = adm_answers.menu
                self.responder(menu)
                self.user.update_information(menu=0, stage=0.0)
            elif self.message == '2':
                message_finality = adm_answers.message_finality
                self.responder(message_finality)
                self.user.reset_user()

    def responder(self, message):
        for answer in message:
            self.text_field.send_keys(answer, self.same_line)
        self.text_field.send_keys('', Keys.ENTER)
