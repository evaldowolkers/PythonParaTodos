from pessoa import Pessoa

# Criado objeto p da classe pessoa passando 'José' para nome
p = Pessoa('José')
print(p.nome) # imprimindo o valor do atributo nome do objeto p

# Criando um método chamado retornar_nome que retorna a propriedade nome (de self)
def pegar_nome(self):
    return self.nome

# Criando o método pegar_nome na classe Pessoa com base no método pegar_nome que criei acima
Pessoa.pegar_nome = pegar_nome

# Executando o método pegar nome do objeto p
print(p.pegar_nome())

#Criando o método mudar_nome
def mudar_nome(self, novo_nome):
    self.nome = novo_nome

# Criando o método mudar_nome na classe Pessoa
Pessoa.mudar_nome = mudar_nome

# Executando o método mudar_nome no objeto p
p.mudar_nome('Maria')

# Criando um método denominado imprimir_ola para imprimir "Olá x", onde x é o valor da propriedade nome
def imprimir_ola(self):
    print("Olá", self.nome)

# Criando o método ola na classe Pessoa com base no método imprimir_ola
Pessoa.ola = imprimir_ola

# Executando o método ola do objeto p
p.ola()