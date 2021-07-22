dicionariob = {'nome':'gabriel', 'idade':21}
print(dicionariob)
print(type(dicionariob))

class DicionarioPersonalizado(dict):
    def pop(self, valor):
        return 0
print()

dicionario_personalizado = DicionarioPersonalizado(dicionariob)
print(dicionario_personalizado)
print(type(dicionario_personalizado))

dicionario_personalizado.pop('nome')
print(dicionario_personalizado)
