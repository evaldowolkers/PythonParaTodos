while True:
    numero = input("Informe um número ou 'sair' para finalizar: ")
    if numero.lower() == "sair":
        print("Sistema finalizado.")
        break

    if int(numero) % 2 == 0:
        print(f"{numero} é um número par.")
    else:
        print(f"{numero} é um número ímpar.")
