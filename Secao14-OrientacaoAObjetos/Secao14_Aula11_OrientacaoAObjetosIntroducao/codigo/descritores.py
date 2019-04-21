class MeuDescritor(object):
    """
    Um exemplo simples de descritor
    """
    def __init__(self, valor_inicial=None, nome='my_var'):
        self.valor = valor_inicial
        self.nome = nome

    def __get__(self, instance, owner):
        print("Obtendo: ", self.nome)
        return self.valor

    def __set__(self, instance, valor):
        print(f"Atribuindo {valor} a {self.nome}");
        self.valor = valor

class MinhaClasse(object):
    descritor = MeuDescritor(valor_inicial='10', nome='dinheiro')
    normal = 20

classe = MinhaClasse()
print(classe.descritor) # Executa o get para imprimir o valor, então imprime a linha do "Obtendo"
print(classe.normal) # Não é um descritor
classe.descritor = 200 # Executa o __set__
print(classe.descritor) # Imprime agora 200