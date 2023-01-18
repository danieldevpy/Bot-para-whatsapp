from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from app.views import middleware
from app.models.crud import get_group
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:\\Users\\Cisbot\\AppData\\Local\\Google\\Chrome\\User Data')
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://web.whatsapp.com/')
action_boll = ActionChains(driver)
time.sleep(15)


def bot():
    try:
        # PEGA A BOLINHA VERDE
        boll = driver.find_elements(By.CLASS_NAME, 'aumms1qt')
        click_boll = boll[-1]
        action_boll.move_to_element_with_offset(click_boll, 0, -20)
        action_boll.click()
        action_boll.perform()
        action_boll.click()
        action_boll.perform()
        # PEGA O TELEFONE DO CLIENTE
        number_client = driver.find_element(By.XPATH, '//*[@id="main"]/header/div[2]/div/div/span')
        number = number_client.text

        # PEGA A MENSAGEM DO CLIENTE
        collect_message = driver.find_elements(By.CLASS_NAME, '_11JPr')
        all_messages = [e.text for e in collect_message]
        message = all_messages[-1]
        # REGISTRANDO CAMPO DE TEXTO
        text_field = driver.find_element(By.XPATH,
                                         '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')

        # # RESPONDENDO
        middleware.Mid(number, message, text_field)

        while True:
            # VOLTAR PARA O CONTATO PADRÃO
            contato_padrao = driver.find_element(By.CLASS_NAME, '_2XH9R')
            acao_contato = webdriver.common.action_chains.ActionChains(driver)
            acao_contato.move_to_element_with_offset(contato_padrao, 0, -20)
            acao_contato.click()
            acao_contato.perform()
            acao_contato.click()
            acao_contato.perform()
            time.sleep(0.2)
            name_fixo = driver.find_element(By.XPATH, '//*[@id="main"]/header/div[2]/div[1]/div/span')
            name = name_fixo.text
            if name == "TI Cisbaf":
                query = get_group()
                if query:
                    same_line = [Keys.SHIFT, Keys.ENTER, Keys.SHIFT]
                    group = driver.find_element(By.XPATH,
                        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
                    message = str(query).split(';')
                    for answer in message:
                        group.send_keys(answer, same_line)
                    group.send_keys('', Keys.ENTER)
                break

    except:
        time.sleep(1)


while True:
    bot()
