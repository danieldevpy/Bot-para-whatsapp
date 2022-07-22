from app.controller import account
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from app.controller.welcome import welcome


class Mid:
    def __init__(self, number, message, text_field):
        self.user = None
        self.number = number
        self.message = message
        self.text_field = text_field
        self.mesma_linha = [Keys.SHIFT, Keys.ENTER, Keys.SHIFT]

        # Creating a user object
        self.user = account.Account(self.number)

        # Checking if the number exists in the database
        search = self.user.get_user()
        # Creating a user in the database, if it does not exist
        if search is None:
            self.user.create_user()

        # checking if the user already has the updated information
        if self.user.active == 0:
            date = int(str(datetime.now())[11:13])
            if date < 12:
                greetings = 'Bom dia'
            elif date < 18:
                greetings = 'Boa Tarde'
            elif date >= 18:
                greetings = 'Boa Noite'
            else:
                greetings = 'Tudo bem?'
            self.text_field.send_keys(
                f'Olá, {greetings}! Sou *CisBoot*, o robô virtual do CISBAF, para começarmos digite o seu *nome*!',
                Keys.ENTER)
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
                f'Porfavor, digite o *número* correspondente ao *setor* com que você deseja falar. ', self.mesma_linha)
                self.text_field.send_keys(
                    f'*1*. Falar com o TI. ', self.mesma_linha)
                self.text_field.send_keys(
                    f'*2*. Falar com o RH. ', Keys.ENTER)

        # checando se o usuario está ativo
        elif self.user.active == 2:
            # caso o usuario não tenha escolhido o setor
            if self.user.level == 0:
                if self.message == '1':
                    pass
                elif self.message == '2':
                    pass
                else:
                    if self.message != '0':
                        sectors = welcome.sectors
                        for answer in sectors:
                            self.text_field.send_keys(answer, self.mesma_linha)
                        self.text_field.send_keys('', self.mesma_linha)

            # caso o usuario tenha escolhido o setor 1
            elif self.user.level == 1:
                menu = self.user.stage[0]
                if menu == 1:
                    pass

            #caso o usuario tenha escolhido o setor 2
            elif self.user.level == 2:
                pass

