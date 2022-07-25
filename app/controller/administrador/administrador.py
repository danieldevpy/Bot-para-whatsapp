from selenium.webdriver.common.keys import Keys


class Adm:
    def __init__(self, user, text_field, message, same_line):
        self.user = user
        self.text_field = text_field
        self.message = message
        self.same_line = same_line

        if self.user.menu == 0:
            if self.message == '1':
                self.text_field.send_keys('Chegou no teste', Keys.ENTER)
                self.user.update_information(menu=1)
