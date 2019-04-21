class Mae(object):
    def __init__(self):
        self.__atributo_privado = 10

class Filha(Mae):
    def pegar_atributo_privado(self):
#        return self.__atributo_privado
        return self._Mae__atributo_privado

filha = Filha()
print(filha.__dict__)
x = filha.pegar_atributo_privado()
print(x)