class Animal():
    # método construtor
    def __init__(self, nome, dono, tipo):
        print('classe instânciada para {}'.format(nome))
        self.nome = nome
        self.dono = dono
        self.tipo = tipo

    def nome(self):
        return self.nome

    def dono(self):
        return self.dono

    def muda_nome(self,novo_nome):
         self.nome = novo_nome

# instanciando a classe
rex = Animal("Rex", "Gabriel", "Cachorro")
mia = Animal("Mia", "mariana", "Gato")

print("\nNome:", rex.nome)
print("Dono:", rex.dono)
print("Tipo:", rex.tipo)
rex.muda_nome("Marlon")
print("Nome:", rex.nome)

print("\nNome:", mia.nome)
print("Dono:", mia.dono)
print("Tipo:", mia.tipo)

