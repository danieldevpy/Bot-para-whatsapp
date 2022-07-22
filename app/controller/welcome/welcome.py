from datetime import datetime
date = int(str(datetime.now())[11:13])
if date < 12:
    hour = 'Bom dia'
elif date < 18:
    hour = 'Boa Tarde'
elif date >= 18:
    hour = 'Boa Noite'
else:
    hour = 'Tudo bem?'

greetings = [f'Olá, {hour}! Sou *CisBoot*, o robô virtual do CISBAF, para começarmos digite o seu *nome*!']

sectors = ['Porfavor, digite o *número* correspondente ao *setor* com que você deseja falar. ', '*1*. Falar com o TI. ',
         '*2*. Falar com o RH. ']

