from app.controller import account
from selenium.webdriver.common.keys import Keys
from app.controller.welcome import welcome
from app.controller.ti import ti_answers


class Mid:
    def __init__(self, number, message, text_field):
        self.user = None
        self.number = number
        self.message = message
        self.text_field = text_field
        self.same_line = [Keys.SHIFT, Keys.ENTER, Keys.SHIFT]

        # Creating a user object
        self.user = account.Account(self.number)

        # Checking if the number exists in the database
        search = self.user.get_user()
        # Creating a user in the database, if it does not exist
        if search is None:
            self.user.create_user()

        # checking if the user already has the updated information
        if self.user.active == 0:
            # mensagem de boas vindas
            greetings = welcome.sectors
            for answer in greetings:
                self.text_field.send_keys(answer, self.same_line)
            self.text_field.send_keys('', Keys.ENTER)
            self.user.update_information(active=1)

        # Caso já tenha recebido a mensagem inicial
        elif self.user.active == 1:
            if self.user.name is None:
                self.user.update_information(name=self.message)
                self.text_field.send_keys(f'*Obrigado {self.user.name}*, me diga qual é a sua *unidade.* ', Keys.ENTER)
            elif self.user.unity is None:
                self.user.update_information(unity=self.message)
                self.text_field.send_keys(f'*Certo, agora me diga qual o seu setor!* ', Keys.ENTER)
            elif self.user.sector is None:
                self.user.update_information(sector=self.message, active=2)
                self.text_field.send_keys(
                    f'Porfavor, digite o *número* correspondente ao *setor* com que você deseja falar. ',
                    self.same_line)
                self.text_field.send_keys(
                    f'*1*. Falar com o TI. ', self.same_line)
                self.text_field.send_keys(
                    f'*2*. Falar com o RH. ', Keys.ENTER)

        # checando se o usuario está ativo
        elif self.user.active == 2:
            # caso o usuario não tenha escolhido o setor
            if self.user.level == 0:
                # caso tenha escolhido o setor 1
                if self.message == '1':
                    menu = ti_answers.menu
                    for answer in menu:
                        self.text_field.send_keys(answer, self.same_line)
                    self.text_field.send_keys('', Keys.ENTER)
                    self.user.update_information(level=1)
                # caso tenha escolhido o setor 2
                elif self.message == '2':
                    pass
                # caso não digitar um numero correspondente a algum setor
                else:
                    if self.message != '0':
                        sectors = welcome.sectors
                        for answer in sectors:
                            self.text_field.send_keys(answer, self.same_line)
                        self.text_field.send_keys('', Keys.ENTER)

            # caso o usuario tenha escolhido o setor 1
            elif self.user.level == 1:
                if self.user.menu == 0:

                    # caso escolher o menu 1
                    if self.message == '1':
                        option_1 = ti_answers.option_1
                        for answer in option_1:
                            self.text_field.send_keys(answer, self.same_line)
                        self.text_field.send_keys('', Keys.ENTER)
                        self.user.update_information(menu=1)

                    # caso escolher o menu 2
                    elif self.message == '2':
                        option_2 = ti_answers.option_2
                        for answer in option_2:
                            self.text_field.send_keys(answer, self.same_line)
                        self.text_field.send_keys('', Keys.ENTER)
                        self.user.update_information(menu=2)

                    # caso escolher o menu 3
                    elif self.message == '3':
                        option_3 = ti_answers.option_3
                        for answer in option_3:
                            self.text_field.send_keys(answer, self.same_line)
                        self.text_field.send_keys('', Keys.ENTER)
                        self.user.update_information(menu=3)

                    # caso escolher o menu 4
                    elif self.message == '4':
                        option_4 = ti_answers.option_4
                        for answer in option_4:
                            self.text_field.send_keys(answer, self.same_line)
                        self.text_field.send_keys('', Keys.ENTER)
                        self.user.update_information(menu=4)

                    # caso escolher o menu 5
                    elif self.message == '5':
                        option_5 = ti_answers.option_5
                        for answer in option_5:
                            self.text_field.send_keys(answer, self.same_line)
                        self.text_field.send_keys('', Keys.ENTER)
                        self.user.update_information(menu=5)

                # caso o usuario já tiver escolhido o menu 1, aqui vão as opções do menu 1
                elif self.user.menu == 1:
                    if self.user.stage == 0.0:
                        if self.message == '1':
                            option_1_1 = ti_answers.option_1_1
                            for answer in option_1_1:
                                self.text_field.send_keys(answer, self.same_line)
                            self.text_field.send_keys('', Keys.ENTER)
                            self.user.update_information(stage=1.0)

                        elif self.message == '2':
                            option_1_2 = ti_answers.option_1_2
                            for answer in option_1_2:
                                self.text_field.send_keys(answer, self.same_line)
                            self.text_field.send_keys('', Keys.ENTER)
                            self.user.update_information(stage=2.0)

                    elif self.user.stage == 1.0:
                        if self.message != '0':
                            self.user.reset_user()
                            self.user.finishing(self.message)

            # caso o usuario tenha escolhido o setor 2
            elif self.user.level == 2:
                pass

            if self.message == '0':
                hello = welcome.sectors
                self.user.reset_user()
                for answer in hello:
                    self.text_field.send_keys(answer, self.same_line)
                self.text_field.send_keys('', Keys.ENTER)
