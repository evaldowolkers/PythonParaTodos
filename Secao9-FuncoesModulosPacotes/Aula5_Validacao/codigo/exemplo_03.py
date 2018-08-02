def valida_elementos(texto, lista):
    if texto.upper() in lista:
        return True
    else:
        print("Opção inválida, veja as opções disponíveis:")
        for item in lista:
            print(item)

while True:
    lista = ["CARRO", "NAVIO", "ÔNIBUS", "AVIÃO"]
    resposta = input("Informe um meio de transporte: ")
    if valida_elementos(resposta, lista):
        break