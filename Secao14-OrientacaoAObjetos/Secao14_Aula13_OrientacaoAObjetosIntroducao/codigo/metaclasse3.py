def meu_metodo(self):
    return 1

MinhaClasse = type('MinhaClasse', (object,), {'metodo': meu_metodo})

instancia = MinhaClasse()
x = instancia.metodo()
print(x)

