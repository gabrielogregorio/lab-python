#instancia -> classe -> metaclasse
# metaclasse instancia da classe
# metaclasse -> Definie como uma classe se comporta
# No python, classe também são objetos
# METACLASS É UMA CLASSE DE FABRICA
# TODAS AS CLASSES NASCEM DA TYPE
# type é a classe builtin que o python usa
'''
# O PYTHON CRIA UM OBJETO
# AUTOMATICAMENTE
class MinhaClasse(object):
    pass

# type é uma metaclasse usada para criar todas as classes
minhaClasse2 = type('MinhaClasse2', (), {'nome':'Gabriel'})
print(MinhaClasse)
print(minhaClasse2)

n = 0
print(n.__class__)
# <class 'int'>

print(n.__class__.__class__)
# <class 'type'>

print()
print()
print()
print()
print()
'''
# METACLASSES HERDAM DE TYPE
# ELAS SÂO CHAMADAS AUTOMATICAMENTE
# ATRAVEZ DE UMA KEYWORLD

class MinhaMetaClasse(type):
    def __new__(cls, clsname, superClasses, atributedict):
        print('clsname:', clsname)
        print('superClasses:', superClasses)
        print('atributedict:', atributedict)

        return type.__new__(cls, clsname, superClasses, atributedict)

class Pai:
    pass

class Mae:
    pass

class Filha(Pai, Mae, metaclass=MinhaMetaClasse):
    pass


obj = Filha()
print(obj.__class__)
print(obj.__class__.__class__)
print(obj.__class__.__class__.__class__)
print(obj.__class__.__class__.__class__.__class__)
