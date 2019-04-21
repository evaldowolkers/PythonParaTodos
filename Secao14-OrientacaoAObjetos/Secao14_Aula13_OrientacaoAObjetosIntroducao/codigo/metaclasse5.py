def inicializador_pessoa(self, nome, sobrenome):
    self.nome = nome
    self.sobrenome = sobrenome


Pessoa = type('Pessoa', (object,), {'__init__': inicializador_pessoa,'a':'Teste','b':10})

print("type(Pessoa):", type(Pessoa))
print("vars(Pessoa):",vars(Pessoa))

pes = Pessoa('Evaldo', 'Wolkers')

print("type(pes):", type(pes))

print(pes.nome)
print(pes.sobrenome)
print(pes.a)
print(pes.b)