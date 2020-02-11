# Criando a lista vazia
lista_numeros = []

# Criando um loop infinito para solicitar vários números
# ao usuário
while True:
    # Alimentando a variável numero com um número informado pelo usuário
    numero = float(input("Informe um número ou zero para sair: "))

    # Se o usuário informar zero, sai do loop com break
    # Caso contrário, vai adicionando o número à lista
    if numero == 0:
        break
    else:
        lista_numeros.append(numero)

# Imprimindo o número na posição zero da lista
print("O primeiro número informado foi:", lista_numeros[0])
# Imprimindo o número na última posição da lista
print("O último número informado foi:", lista_numeros[-1])
# Imprimindo a soma dos números, formatada para float e
# com duas decimais
print(f"A soma dos números informados é: {sum(lista_numeros):.2f}")
# Imprimindo a média dos números informados, formatada para float
# e com duas decimais
print(f"A média dos números informados é: {sum(lista_numeros) / len(lista_numeros):.2f}")

# Criando as variáveis para armazenamento das informações
num_mais = 0 # Vai armazenar o número que aparece mais vezes
qtd_mais = 1 # Vai armazenar quantas vezes o número apareceu
tem_mais = False # Variável de controle
lista_pares = [] # Vai armazenar os números pares
lista_impares = [] # Vai armazenar os números ímpares

# Percorrendo os números da lista e armazenando em "numero"
for numero in lista_numeros:
    # Verificando se o resto da divisão do número por dois é zero
    # Se for, adicionado na lista de números pares
    # Caso contrário, adiciona na lista de números ímpares
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

    # Pegando a quantidade de vezes que o número aparece na lista
    qtd = lista_numeros.count(numero)
    # Se a quantidade encontrada for maior que o conteúdo de
    # qtd_mais, vai armazenar a quantidade encontrada na variável
    # qtd_mais, vai armazenar o número em num_mais, para sabermos
    # qual número tem mais ocorrências e vai mudar a variável
    # tem_mais para true, para sabermos que existe um número que
    # aparece mais que outros
    if qtd > qtd_mais:
        tem_mais = True
        qtd_mais = qtd
        num_mais = numero

# Agora vamos imprimir as informações solicitadas

# Se a variável tem_mais for True, vai imprimir o número que
# aparece mais vezes
if tem_mais:
    print("O número que mais apareceu foi:", num_mais)

# Se tem conteúdo na lista_pares,
# vai imprimir a lista de números pares
if lista_pares:
    print("Números pares:", lista_pares)

# Se tem conteúdo na lista_impares,
# vai imprimir a lista de números ímpares
if lista_impares:
    print("Números ímpares:", lista_impares)

# Imprimindo a lista completa
print("Lista completa:", lista_numeros)

# Invertendo os números na lista e imprimindo invertida
lista_numeros.reverse()
print("Lista em ordem inversa:", lista_numeros)

# Ordenando os números na lista e imprimindo ordenado
lista_numeros.sort()
print("Lista em ordem crescente:", lista_numeros)
