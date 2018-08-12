contador = 0
palavra = input("Informe a palavra a ser pesquisada: ")
nome_arquivo = input("Informe o nome do arquivo: ")
with open(nome_arquivo, "r") as arquivo:
    for linha in arquivo:
        contador = contador + linha.upper().count(palavra.upper())

print("Palavra pesquisada: " + palavra.upper())
print("Arquivo pesquisado: " + nome_arquivo)
print("Total de palavras encontradas: " + str(contador))