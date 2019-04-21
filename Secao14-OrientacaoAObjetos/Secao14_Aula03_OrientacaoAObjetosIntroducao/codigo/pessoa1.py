class Pessoa():
    especies = 'Humano'

print(Pessoa.especies) # Humano
Pessoa.vivo = True # Adicionado dinamicamente
print(Pessoa.vivo) # True
homem = Pessoa()
print(homem.especies) # Humano (herdado)
print(homem.vivo) # True (herdado)
Pessoa.vivo = False
print(homem.vivo) # False (herdado)
homem.nome = 'Evaldo'
homem.sobrenome = 'Wolkers'
print(homem.nome, homem.sobrenome) # Evaldo Wolkers