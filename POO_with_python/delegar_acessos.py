class A:
    def fazer_algo(self):
        print('fazerAlgo')

    def metodo_que_nao_existe_em_b(self, nome):
        print('Só existo no A', nome)

class B:
    def __init__(self):
        self.a = A()

    # Forma 1
    def fazer_algo(self):
        # Delegar para self.a
        return self.a.fazer_algo()

    # Forma 2
    def __getattr__(self, nome):
        return getattr(self.a, nome)

b = B()
b.fazer_algo()
b.metodo_que_nao_existe_em_b('Gabscleison')
