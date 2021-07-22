# Classe que nao possui método implementado.
# Também chamado de interface

from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def dizer_algo(self):
        # Pode retornar algo sim e chamar com o super(Cachorro, self).dizer_algo()
        pass

# VOCE É FORCADO A IMPLEMENTAR
class Cachorro(Animal):
    def latir(self):
        print('auau')

    def dizer_algo(self):
        return 'AuAU'

c = Cachorro()
c.latir()
# Não pode ser instanciada
# obj = ClasseAbstrata()
# Use com moderação
