import re
texto = '2 + 23 - 232 + 1342 / 23 * ( 232 - 23 ** 9) % 2'

for valor in re.finditer(' ',texto):
    print(valor.start(),valor.end())

