status = int(input("Informe o código do status (1-4): "))
quantidade_malas = int(input("Informe o número de malas: "))

if ((status == 1 and quantidade_malas > 1) or (status == 2 and quantidade_malas > 2) or
        ((status == 3 or status == 4) and quantidade_malas > 3)):
    print("Você terá que pagar uma taxa de serviço por excesso de bagagem!")
else:
    comprimento = int(input("Informe o comprimento da mala 1 (cm): "))
    largura = int(input("Informe a largura da mala 1 (cm): "))
    altura = int(input("Informe a altura da mala 1 (cm): "))
    peso = float(input("Informe o peso da mala 1 (kg): "))

    if ((comprimento + largura + altura) > 158) or (peso > 32):
        print("Você terá que pagar uma taxa de serviço por excesso de bagagem!")
    else:
        if quantidade_malas > 1:
            comprimento = int(input("Informe o comprimento da mala 2 (cm): "))
            largura = int(input("Informe a largura da mala 2 (cm): "))
            altura = int(input("Informe a altura da mala 2 (cm): "))
            peso = float(input("Informe o peso da mala 2 (kg): "))

            if ((comprimento + largura + altura) > 158) or (peso > 32):
                print("Você terá que pagar uma taxa de serviço por excesso de bagagem!")
            else:
                if quantidade_malas > 2:
                    comprimento = int(input("Informe o comprimento da mala 3 (cm): "))
                    largura = int(input("Informe a largura da mala 3 (cm): "))
                    altura = int(input("Informe a altura da mala 3 (cm): "))
                    peso = float(input("Informe o peso da mala 3 (kg): "))

                    if ((comprimento + largura + altura) > 158) or (peso > 32):
                        print("Você terá que pagar uma taxa de serviço por excesso de bagagem!")
                    else:
                        print("Tudo ok com as bagagens, tenha uma boa viagem.")
                else:
                    print("Tudo ok com as bagagens, tenha uma boa viagem.")
        else:
            print("Tudo ok com as bagagens, tenha uma boa viagem.")