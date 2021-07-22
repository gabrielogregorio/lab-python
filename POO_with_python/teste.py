class Peca():
    def __init__(self):
        pass

    def mover(self, pos):
        print('pos', pos)


class Dama(Peca):
    def __init__(self):
        Peca.__init__(self)

    def mover(self):
        print('x9')

a = Dama()
a.mover()
a.mover('oi')