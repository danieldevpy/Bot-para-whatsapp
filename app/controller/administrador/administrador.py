from selenium.webdriver.common.keys import Keys
from app.controller.account import Account
import adm_answers

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
                awnser = str(self.message).split(',')
                detail = adm_answers.detail
                user = Account(awnser[0])
                if len(awnser) == 2:
                    user.update_information(name=awnser[1])
                elif len(awnser) == 3:
                    user.update_information(name=awnser[1], unity=awnser[2])
                elif len(awnser) == 4:
                    user.update_information(name=awnser[1], unity=awnser[2], sector=awnser[3])
                self.responder(detail)
                self.user.update_information(menu=9)
        elif self.user.menu == 2:
            user = Account(self.message)
            user.update_information(level=777)
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
