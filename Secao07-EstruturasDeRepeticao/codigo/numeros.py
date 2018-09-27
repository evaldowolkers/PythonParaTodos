quantidadeNumeros = int(input("Informe a qtd. de números de 1 a 9: "))

numeroFinal = 0

if quantidadeNumeros < 1 or quantidadeNumeros > 9:
    print("Quantidade de números inválida!")
else:
    contador = 1
    while contador <= quantidadeNumeros:
        if contador == 1:
            posicao = "primeiro"
        elif contador == 2:
            posicao = "segundo"
        elif contador == 3:
            posicao = "terceiro"
        elif contador == 4:
            numero = "quarto"
        elif contador == 5:
            posicao = "quinto"
        elif contador == 6:
            posicao = "sexto"
        elif contador == 7:
            posicao = "sétimo"
        elif contador == 8:
            posicao = "oitavo"
        else:
            posicao = "nono"

        numero = int(input("Informe o " + posicao + " número: "))
        print(f"Você informou {numero}, o resultado será {numero * contador}")

        numeroFinal += numero * contador
        contador += 1

    print(f"O resultado final é: {numeroFinal}")


