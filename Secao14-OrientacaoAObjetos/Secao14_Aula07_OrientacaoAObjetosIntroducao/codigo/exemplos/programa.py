from pessoa import Pessoa

p = Pessoa("José")

def pegar_nome(self):
    return self.nome

Pessoa.pegar_nome = pegar_nome

def mudar_nome(self, novo_nome):
    self.nome = novo_nome

Pessoa.mudar_nome = mudar_nome

p.mudar_nome("Evaldo")

Pessoa.sobrenome = "Wolkers"

def imprimir_ola(self):
    print("Olá", self.nome, self.sobrenome)

Pessoa.ola = imprimir_ola

p.ola()

