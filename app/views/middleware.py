from selenium.webdriver.common.keys import Keys
from datetime import datetime
from threading import Thread
from app.controller import account
from app.controller.administrador import adm_answers, administrador
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
            date = int(str(datetime.now())[11:13])
            if date < 12:
                hour = 'Bom dia'
            elif date < 18:
                hour = 'Boa Tarde'
            elif date >= 18:
                hour = 'Boa Noite'
            else:
                hour = 'Tudo bem?'

            self.text_field.send_keys(
                f'*Olá*, {hour}! Sou *CisBoot*, o robô virtual do *CISBAF*.',
                self.same_line)
            self.text_field.send_keys(
                f'Percebo que esse é o nosso primeiro contato, então aqui vai uma dica! ⬇',
                self.same_line)
            self.text_field.send_keys(
                f'Eu converso com as pessoas por etapas, então para começarmos diga o seu *nome* por favor!',
                Keys.ENTER)
            self.user.update_information(active=1)

        # Caso já tenha recebido a mensagem inicial
        elif self.user.active == 1:
            if self.user.name is None:
                self.user.update_information(name=self.message)
                self.text_field.send_keys(f'Obrigado *{self.user.name}*, me diga qual é a sua *unidade.* ', Keys.ENTER)
            elif self.user.unity is None:
                self.user.update_information(unity=self.message)
                self.text_field.send_keys(f'Certo, agora me diga qual o seu *setor!* ', Keys.ENTER)
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
        elif self.user.active == 2 and self.message != '0':
            # caso o usuario não tenha escolhido o setor
            if self.user.level == 0:
                # caso tenha escolhido o setor 1
                if self.message == '1':
                    menu = ti_answers.menu
                    self.responder(menu)  # reposta
                    self.user.update_information(level=1)
                # caso tenha escolhido o setor 2
                elif self.message == '2':
                    pass
                # caso for adm
                elif self.message == '7890380':
                    menu_adm = adm_answers.menu
                    self.responder(menu_adm)  # resposta
                    self.user.update_information(level=10)

                # caso não digitar um numero correspondente a algum setor
                else:
                    if self.message != '0':
                        self.text_field.send_keys(
                            f'Porfavor, digite o *número* correspondente ao *setor* com que você deseja falar. ',
                            self.same_line)
                        self.text_field.send_keys(
                            f'*1*. Falar com o TI. ', self.same_line)
                        self.text_field.send_keys(
                            f'*2*. Falar com o RH. ', Keys.ENTER)
                # caso o usuario tenha escolhido o setor 1
            elif self.user.level == 1:
                if self.user.menu == 0:

                    # caso escolher o menu 1
                    if self.message == '1':
                        option_1 = ti_answers.option_1
                        self.responder(option_1)  # reposta
                        self.user.update_information(menu=1)

                    # caso escolher o menu 2
                    elif self.message == '2':
                        option_2 = ti_answers.option_2
                        self.responder(option_2)  # reposta
                        self.user.update_information(menu=2)

                    # caso escolher o menu 3
                    elif self.message == '3':
                        option_3 = ti_answers.option_3
                        self.responder(option_3)  # reposta
                        self.user.update_information(menu=3)

                    # caso escolher o menu 4
                    elif self.message == '4':
                        option_4 = ti_answers.option_4
                        self.responder(option_4)  # reposta
                        called = 'Atualização de whatsapp'
                        self.user.finishing(called)
                        self.user.reset_user()

                    # caso escolher o menu 5
                    elif self.message == '5':
                        option_5 = ti_answers.option_5
                        self.responder(option_5)  # reposta
                        self.user.update_information(menu=5)

                    else:
                        message_except = ti_answers.message_excep
                        self.responder(message_except)
                # caso o usuario já tiver escolhido o menu 1, aqui vão as opções do menu 1
                elif self.user.menu == 1:
                    # estado inicial do menu 1
                    if self.user.stage == 0.0:
                        if self.message == '1':
                            option_1_1 = ti_answers.option_1_1
                            self.responder(option_1_1)  # reposta
                            self.user.update_information(stage=1.0)

                        elif self.message == '2':
                            option_1_2 = ti_answers.option_1_2
                            self.responder(option_1_2)  # reposta
                            self.user.update_information(stage=2.0)
                        else:
                            message_except = ti_answers.message_excep
                            self.responder(message_except)
                    # 3stagio 1.0
                    elif self.user.stage == 1.0:
                        if self.message != '0':
                            message_finality = ti_answers.message_finality
                            self.responder(message_finality)  # reposta
                            called = f'Problema na hora do login: {self.message}'
                            self.user.finishing(called)
                            self.user.reset_user()

                    # estagio 2.0
                    elif self.user.stage == 2.0:
                        option_1_2_1 = ti_answers.option_1_2_1
                        self.responder(option_1_2_1)  # reposta
                        called = f'Criação de login, Nome: {self.message}'
                        self.user.update_information(message=called, stage=2.1)

                    elif self.user.stage == 2.1:
                        option_1_2_2 = ti_answers.option_1_2_2
                        self.responder(option_1_2_2)  # reposta
                        called = f'{self.user.message}, CPF: {self.message}'
                        self.user.update_information(message=called, stage=2.2)

                    elif self.user.stage == 2.2:
                        option_1_2_3 = ti_answers.option_1_2_3
                        self.responder(option_1_2_3)  # reposta
                        called = f'{self.user.message}, Cargo: {self.message}'
                        self.user.update_information(stage=2.3)
                        self.user.finishing(called)

                    elif self.user.stage == 2.3:
                        if self.message == '1':
                            option_1_2 = ti_answers.option_1_2
                            self.responder(option_1_2)  # reposta
                            self.user.update_information(stage=2.0)
                        elif self.message == '2':
                            message_finality = ti_answers.message_finality
                            self.responder(message_finality)  # reposta
                            self.user.reset_user()
                        else:
                            option_1_2_3 = ti_answers.option_1_2_3
                            self.responder(option_1_2_3)  # reposta
                    else:
                        message_except = ti_answers.message_excep
                        self.responder(message_except)
                # menu escolhido 2
                elif self.user.menu == 2:
                    # estado inicial do menu 2
                    if self.user.stage == 0.0:
                        if self.message == '1':
                            self.user.update_information(stage=1.1, message='Ocorrencia não chega')
                        elif self.message == '2':
                            self.user.update_information(stage=1.1, message='Ocorrencia travada')
                        elif self.message == '3':
                            self.user.update_information(stage=1.1, message='Não consigo logar no sistema')
                        elif self.message == '4':
                            detail = ti_answers.detail
                            self.responder(detail)  # reposta
                            self.user.update_information(stage=1.4, message='Problema fisíco no tablet')
                        elif self.message == '5':
                            message_finality = ti_answers.message_finality
                            self.responder(message_finality)  # reposta
                            called = 'O tablet não está carregando!'
                            self.user.finishing(called)
                            self.user.reset_user()
                        else:
                            message_except = ti_answers.message_excep
                            self.responder(message_except)
                        if self.user.stage == 1.1:
                            option_2_123 = ti_answers.option_2_123
                            self.responder(option_2_123)  # reposta
                    elif self.user.stage == 1.1:
                        if self.message == '1':
                            option_2_1_1 = ti_answers.option_2_1_1
                            self.responder(option_2_1_1)  # reposta
                            self.user.reset_user()
                        elif self.message == '2':
                            message_finality = ti_answers.message_finality
                            self.responder(message_finality)
                            called = self.user.message
                            self.user.finishing(called)
                            self.user.reset_user()
                        else:
                            message_except = ti_answers.message_excep
                            self.responder(message_except)

                    elif self.user.stage == 1.4:
                        called = f'{self.user.message} {self.message}'
                        message_finality = ti_answers.message_finality
                        self.responder(message_finality)
                        self.user.finishing(called)
                        self.user.reset_user()
                    else:
                        message_except = ti_answers.message_excep
                        self.responder(message_except)
                elif self.user.menu == 3:
                    # estado inicial do menu 3
                    if self.user.stage == 0.0:
                        if self.message == '1':
                            self.user.update_information(stage=1.1, message='Suporte para o computador')
                        elif self.message == '2':
                            self.user.update_information(stage=1.1, message='Suporte para a impressora')
                        elif self.message == '3':
                            self.user.update_information(stage=1.1, message='Outros')
                        else:
                            message_except = ti_answers.message_excep
                            self.responder(message_except)
                        if self.user.stage == 1.1:
                            detail = ti_answers.detail
                            self.responder(detail)
                    elif self.user.stage == 1.1:
                        message_finality = ti_answers.message_finality
                        self.responder(message_finality)
                        called = f'{self.user.message}: {self.message}'
                        self.user.finishing(called)
                        self.user.reset_user()
                    else:
                        message_except = ti_answers.message_excep
                        self.responder(message_except)

                elif self.user.menu == 5:
                    if self.user.stage == 0.0:
                        called = f'Falar com TI: {self.message}'
                        message_finality = ti_answers.message_finality
                        self.responder(message_finality)
                        self.user.finishing(called)
                        self.user.reset_user()

            # caso o usuario tenha escolhido o setor 2
            elif self.user.level == 2:
                pass

            # caso o usuário esteja como adm
            elif self.user.level == 10:
                administrador.Adm(user=self.user, text_field=self.text_field,
                                  message=self.message, same_line=self.same_line)

        # caso o usuário digite 0 em qualquer menu, cairá aqui!
        if self.message == '0':
            self.text_field.send_keys(
                f'{self.user.name} você voltou ao menu!'
                f' Digite o *número* correspondente ao *setor* com que você deseja falar. ',
                self.same_line)
            self.text_field.send_keys(
                f'*1*. Falar com o TI. ', self.same_line)
            self.text_field.send_keys(
                f'*2*. Falar com o RH. ', Keys.ENTER)
            self.user.update_information(level=0, menu=0, stage=0, message='null', active=2)

        elif self.user.active == 3:
            self.text_field.send_keys(
                f'Olá {self.user.name}, digite o *número* correspondente ao *setor* com que você deseja falar. ',
                self.same_line)
            self.text_field.send_keys(
                f'*1*. Falar com o TI. ', self.same_line)
            self.text_field.send_keys(
                f'*2*. Falar com o RH. ', Keys.ENTER)
            self.user.update_information(active=2)

    def responder(self, message):
        for answer in message:
            self.text_field.send_keys(answer, self.same_line)
        self.text_field.send_keys('', Keys.ENTER)
