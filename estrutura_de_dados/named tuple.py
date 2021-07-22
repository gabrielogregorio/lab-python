from collections import namedtuple
"""
   Acessa os elementos pelo nome
   Suporta todas as operações de tupla
   É imultável igual a uma tupla
   Pode substituir um dicionário PARA USAR
   DE FORMA FIXA E IMUTAVEL.
   MAIS DE DESEMPENHO E OCULPA MENOS ESPACO
"""
Subscriber = namedtuple('NomeDanamedtuple', ['id', 'email'])
sub = Subscriber('1000', 'gabriel.gregorio.1@outlook.com')

print(sub.id)
print(sub.email)
print(sub)
sub1 = sub._replace(id=1001)
print(sub1, sub)