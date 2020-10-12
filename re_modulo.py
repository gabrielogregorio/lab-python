import re

texto = 'PA, pa, Pa, pa, ra'
texto2 = re.sub('pa', 'python', texto, flags=re.IGNORECASE)
print(texto2)

data = '11/04/2020'

import time


# O MATCH SEMPRE TENTA BUSCAR NO INICIO DA STRING

start = time.time()
r = True if re.match(r'\d+/\d+/\d+', data) else False
print(r)
fim = time.time()
print(fim - start)

# Pre compilar e gerar um objeto
# Referente a este padrão
date_pattern = re.compile(r'\d+/\d+/\d+')

start = time.time()
r = True if re.match(date_pattern, data) else False
print(r)
fim = time.time()
print(fim - start)


texto = '12/11/2020 e 10/02/2015'
print(date_pattern.findall(texto))
