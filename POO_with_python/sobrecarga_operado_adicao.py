print(10 + 10)
print('é igual a')
print(10 .__add__(10))

class Operador():
    def __init__(self, num):
        self.num = num

    def __add__(self, op):
        return '[] -> {}'.format(self.num + op.num)

    def __mul__(self, op):
        return '[] -> {}'.format(self.num * op.num)

    def __sub__(self, op):
        return '[] -> {}'.format(self.num - op.num)

op1 = Operador(10)
op2 = Operador(2)

print(op1 + op2)
print(op1 - op2)
print(op1 * op2)
