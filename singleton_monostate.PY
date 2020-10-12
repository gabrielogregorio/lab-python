class MinhaClasse:
    __estado_compartilhado = {"LING":"PYTHON"}

    def __init__(self):
        self.x = 1
        self.__dict__= self.__estado_compartilhado


b1 = MinhaClasse()
b2 = MinhaClasse()
b3 = MinhaClasse()

print(b1)
print(b2)
print(b3)
b2.x = 10

print(b1.__dict__)
print(b2.__dict__)
print(b3.__dict__)

'''
<__main__.MinhaClasse object at 0x7f1d5e5206a0>
<__main__.MinhaClasse object at 0x7f1d5e51efd0>
<__main__.MinhaClasse object at 0x7f1d5e5002b0>
{'LING': 'PYTHON', 'x': 10}
{'LING': 'PYTHON', 'x': 10}
{'LING': 'PYTHON', 'x': 10}
'''