def calculaQuadrado(numero):
    return f"O quadrado de {numero} é: {numero * numero}"

lista_numeros = [1, 2, 3, 4, 5, 6]
calculo = map(calculaQuadrado, lista_numeros)

for n in calculo:
    print(n)