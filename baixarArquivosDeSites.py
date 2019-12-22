# pip install requests
# pip install bs4

from bs4 import BeautifulSoup
from os.path import basename

import requests
import os

def obterHTML(link_site):

    # Faça uma requisição
    r = requests.get(link_site)

    # obtenha o HTML
    return BeautifulSoup(r.content,'html.parser')
    

# Lista com os sites
lista2 = ["https://pixabay.com/images/search/montanhas/","https://pixabay.com/images/search/carros/"]

# Para cada site:
for site in lista2:
    # Obtenha o HTML
    html = obterHTML(site)

    # Defina o diretório como o nome da página do site
    diretorio = site.split(".com/")

    # Corrija problemas com o nome de forma local
    pasta = diretorio[1].replace('/','')

    # Tente criar uma pasta
    os.mkdir(pasta)

    # Ande por todas as tags do site
    for link in html.select("img"):

        # Se tiver src, que é um link, na tag img
        if 'src=' in str(link):

            # Obtenha o atributo src, que contém o link das imagens
            lnk = link['src']

            # Se contiver uma imagem
            if '.jpg' in lnk or 'png' in lnk or 'jpeg' in lnk:

                # Obtenha o nome da imagem, corrigindo problemas
                name = lnk.split('/')

                # baixe o arquivo com o ultimo nome na imagem
                with open(pasta+"/"+name[-1],'wb') as f:
                    # Criar o arquivo localmelmente
                    f.write(requests.get(lnk).content)

                print('Imagem {} Obtida do site {} na pasta {}'.format(name[-1],site, pasta))

