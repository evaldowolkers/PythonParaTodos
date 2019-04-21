class RevelarAcesso(object):
    """Um descritor de dados que define e retorna valores
    normalmente e imprime uma mensagem registrando seu acesso.
    """
    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print('Recuperando', self.name)
        return self.val

    def __set__(self, obj, val):
        print('Atualizando', self.name)
        self.val = val

class MinhaClasse(object):
    x = RevelarAcesso(10, 'var "x"')
    y = 5

m = MinhaClasse()

print("x: ", m.x)
m.x = 20
print("x: ", m.x)

print("y: ", m.y)
m.y = 8
print("y: ", m.y)