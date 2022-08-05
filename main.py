from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from app.views import middleware
from app.models.crud import get_group


driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

time.sleep(15)


def bot():
    try:
        # PEGA A BOLINHA VERDE
        boll = driver.find_elements_by_class_name('aumms1qt')
        click_boll = boll[-1]
        action_boll = webdriver.common.action_chains.ActionChains(driver)
        action_boll.move_to_element_with_offset(click_boll, 0, -20)
        action_boll.click()
        action_boll.perform()
        action_boll.click()
        action_boll.perform()

        # PEGA O TELEFONE DO CLIENTE
        number_client = driver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div[1]/div/span')
        number = number_client.text

        # PEGA A MENSAGEM DO CLIENTE
        collect_message = driver.find_elements_by_class_name('_1Gy50')
        all_messages = [e.text for e in collect_message]
        message = all_messages[-1]

        # REGISTRANDO CAMPO DE TEXTO
        text_field = driver.find_element_by_xpath(
            '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')

        # # RESPONDENDO
        middleware.Mid(number, message, text_field)

        while True:
            # VOLTAR PARA O CONTATO PADRÃO
            contato_padrao = driver.find_element_by_class_name('_2XH9R')
            acao_contato = webdriver.common.action_chains.ActionChains(driver)
            acao_contato.move_to_element_with_offset(contato_padrao, 0, -20)
            acao_contato.click()
            acao_contato.perform()
            acao_contato.click()
            acao_contato.perform()
            time.sleep(0.2)
            name_fixo = driver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div[1]/div/span')
            name = name_fixo.text
            if name == "Clarooo":
                query = get_group()
                if query:
                    group = driver.find_element_by_xpath(
                        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
                    group.send_keys(str(query), Keys.ENTER)
                break

    except:
        time.sleep(1)



while True:
    bot()
