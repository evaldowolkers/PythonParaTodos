numero = int(input("Qual tabuada você quer treinar? Informe o número: "))

acertos = 0
erros = 0

for n in range(1, 11):
    resposta = int(input(f"{numero} x {n} = ? "))
    if resposta == (numero * n):
        print("Correto!!!")
        acertos = acertos + 1
    else:
        print(f"Que pena, você errou, o valor correto é {numero * n}")
        erros = erros + 1

print(f"Total de acertos: {acertos}")
print(f"Total de erros: {erros}")