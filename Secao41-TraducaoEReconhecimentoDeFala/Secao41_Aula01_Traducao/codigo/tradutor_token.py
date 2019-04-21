from googletrans.gtoken import TokenAcquirer

acquirer = TokenAcquirer()
texto = 'Olá!'
tk = acquirer.do(texto)
print(tk)
