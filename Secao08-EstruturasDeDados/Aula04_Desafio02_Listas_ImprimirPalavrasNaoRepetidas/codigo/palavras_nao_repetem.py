lista_palavras = []
lista_nao_repetidas = []
while True:
    palavra = input("Informe uma palavra ou o número zero para sair (repita algumas palavras): ")

    if palavra == "0":
        break
    else:
        lista_palavras.append(palavra)

for palavra in lista_palavras:
    if lista_palavras.count(palavra) == 1:
        lista_nao_repetidas.append(palavra)


print(lista_nao_repetidas)