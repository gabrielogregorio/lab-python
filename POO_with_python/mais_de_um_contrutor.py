class Pessoa:
    # Construtor 1
    def __init__(self, nome):
        print('Construtor 1')
        self.nome = nome

    # Construtor 2
    # Para mais de um construtor, o __init__ deve ser o mais simples possível
    @classmethod
    def contrutor2(cls, nome):
        print('Construtor 2')
        return cls(nome)


#p = Pessoa('Gabriel')
#print(p.nome)

p = Pessoa.contrutor2('Julia')
print(p.nome)
