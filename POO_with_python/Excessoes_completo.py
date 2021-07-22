class SomentePares(list):
    """Esse negócio manipula listas"""

    def append(self, inteiro):
        '''Estou no controle'''
        if not isinstance(inteiro, int):
            raise TypeError('Somente inteiros permitidos')

        if inteiro % 2:
            raise ValueError("Somente Pares são permitidos")

        if inteiro == 10:
            raise ValueError('Numero 10 não permitido!')

        super().append(inteiro)


sp = SomentePares()


try:
    sp.append(10)

except ValueError as erro:
    print("OPS - {}".format(erro.args))

except TypeError as erro2:
    print("OPS - {}".format(erro2))

print(sp)
sp.append(4)
print(sp)
print(help(sp.append))