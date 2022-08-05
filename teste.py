import requests
import threading

open_glpi = lambda: print(requests.get('https://api.github.com'))
threading.Thread(target=open_glpi).start()
