import requests
import time

payload = {
    'nomeDoCampo': 'seu login',
    'nomeDoCampo': 'sua senha',
    'nomeDoCampo': 'login'}

def fazerLogin(payload):
    with requests.Session() as s:
        p = s.post("Link da pagina do roteador",data=payload)

while True:
    try:
        fazerLogin(payload)
    except:
        i = input('logado!')
        break
    else:
        print("Tentando fazer Login")

    time.sleep(1)
