import threading
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from app.views import middleware
from app.models.crud import get_group
import uvicorn

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=~/.config/google-chrome')
driver = webdriver.Chrome(chrome_options=options, service=ChromeService(ChromeDriverManager().install()))
driver.get('https://web.whatsapp.com/')
action_boll = ActionChains(driver)
contato_padrao = None
time.sleep(15)



def bot():
    global contato_padrao
    try:
        # PEGA A BOLINHA VERDE
        boll = driver.find_elements(By.CLASS_NAME, 'aumms1qt')
        click_boll = boll[-1]
        click_boll.click()
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

        # VOLTAR PARA O CONTATO PADRÃO
        if not contato_padrao:
            contato_padrao = driver.find_element(By.CLASS_NAME, "_2H6nH")
            contato_padrao.click()

        contato_padrao.click()
        time.sleep(0.2)
    except:
        query = get_group()
        if query:
            same_line = [Keys.SHIFT, Keys.ENTER, Keys.SHIFT]
            group = driver.find_element(By.XPATH,
                '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
            message = str(query).split(';')
            for answer in message:
                group.send_keys(answer, same_line)
            group.send_keys('', Keys.ENTER)
        time.sleep(1)


def start_bot():
    while True:
        bot()



if __name__ == "__main__":
    threading.Thread(target=start_bot).start()
    print('inciiando uvicorn?')
    uvicorn.run("api:app", host="0.0.0.0", port=8000)
