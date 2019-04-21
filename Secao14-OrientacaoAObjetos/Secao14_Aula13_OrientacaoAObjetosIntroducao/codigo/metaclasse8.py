def fabrica_de_funcoes(nome_metodo, retorno):
    def metodo_criado(self):
        return retorno

    metodo_criado.__name__ = nome_metodo
    return metodo_criado

class MinhaMetaClasse(type):
    def __new__(mcs, nome, bases, atributos):
        for nome, retorno in (('metodo1', 'Olá'), ('metodo2', 'Como vai você?'), ('metodo3', 30 + 40), ('metodo4', str(70 * 7))):
            atributos[nome] = fabrica_de_funcoes(nome, retorno)

        return super().__new__(mcs, nome, bases, atributos)

class MinhaClasse(metaclass=MinhaMetaClasse):
    pass

print("vars(MinhaClasse):",vars(MinhaClasse))
mc = MinhaClasse()
print(mc.metodo1())
print(mc.metodo2())
print(mc.metodo3())
print(mc.metodo4())
