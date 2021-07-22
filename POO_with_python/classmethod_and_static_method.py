class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        print(self)

    # Recebe a classe como primeiro argumento
    # Cria uma instância da propria classe (cls)
    @classmethod
    def de_string(cls, data_string): #10-10-2021
        dia, mes, ano = map(int, data_string.split('-'))
        data = cls(dia, mes, ano)
        return data

    # Não é herdado
    # É uma função estática
    @staticmethod
    def is_data_valid(data_string):
        dia, mes, ano = map(int, data_string.split('-'))
        return dia <= 31 and mes <=12 and ano <= 2030

data = Data(10, 10, 10)

data_str = '10-10-2012'
# Cria uma nova instância
data.de_string(data_str)
print(data.is_data_valid(data_str))


