import requests

cep = input("Digite um cep para consulta: ")

if ((not cep.isnumeric()) or (len(cep) != 8)):
    print("Cep inválido")
    exit()

request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))

dic = request.json()

if 'erro' in dic.keys():
    print('erro')
else:
    print('CEP         : {}'.format(dic['cep']))
    print('Localidade  : {}'.format(dic['localidade']))
    print('UF          : {}'.format(dic['uf']))


