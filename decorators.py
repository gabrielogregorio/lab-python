class paramaiusculo(object):
    # Instância passando a função
    def __init__(self,funcao):
        pass

    # passando argumentos da função quando ela for chamada
    def __call__(self,*argumentos):
        return argumentos[0].upper()

# Muda o comportamento da função
@paramaiusculo
def mostrar(nome):
    return nome

print(mostrar("Mariana"))
