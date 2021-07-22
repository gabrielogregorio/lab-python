import pickle
import json

'''
class Animal(object):
  def __init__(self, idade):
    self.idade = idade
  
  def consultar(self):
    return 'Olá'

inst = Animal(idade=21)
print(inst.consultar())

meus_dados = ['Gabriel', inst]
print(meus_dados[1].consultar())

with open('arquivo.txt', 'wb') as file:
  pickle.dump(meus_dados, file)


with open('arquivo.txt', 'rb') as file:
  dados = pickle.load(file)

print(dados[1].consultar())'''
# ============================= #
#    Serializacao com json      #
# ============================= #

class Contato:
  def __init__(self, primeito_nome):
    self.primeito_nome = primeito_nome

  @property
  def nome(self):
    return 'Olá seu nome é ' + self.primeito_nome

c = Contato('Gabriel')
print(json.dumps(c.__dict__))
