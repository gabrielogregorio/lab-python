# Retorna a ordem das classes da direita para esquerda
# em heranca multipla. Todas as classes herdam de object
class Programador():
    pass

class Pai(Programador):
    def result():
        return'pai'

class Mae(Programador):
    def result():
        return'mae'

class Filha(Pai, Mae):
    # super usa o MRO
    pass

print(Programador.__mro__)

print(Pai.__mro__)
print(Mae.mro())
print(Filha.mro())
print(Filha.result())
