'''
Fazendo métodos em A ficarem disponíveis em B
'''

class A:
    def metodo1(self):
        print("metodo1 disponível em A")

    def metodo2(self, valor):
        print("metodo2 disponível em A =", valor)

    def metodo3(self, nome, idade, sexo):
        print("metodo3 disponível em A =", nome, idade, sexo)

class B:
    def __init__(self):
        self.a = A()

    def metodo1(self):
        print("metodo1 disponível em B")

    def __getattr__(self, *args):
        return getattr(self.a, *args)


test = B()
test.metodo1()
test.metodo2('ola')
test.metodo3('gabriel', 22, 'M')