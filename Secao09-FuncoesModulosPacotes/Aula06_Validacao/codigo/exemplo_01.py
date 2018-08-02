def validar_faixa(numero, inicio, fim):
    if numero.isdigit():
        if int(numero) < int(inicio) or int(numero) > int(fim):
            print(f"Valor inválido! Informe um número inteiro entre {inicio} e {fim}.")
        else:
            return True
    else:
        print(f"Número inválido! Informe um número inteiro entre {inicio} e {fim}.")

while True:
    resposta = input("Informe um número inteiro entre 1 e 10: ")
    if validar_faixa(resposta, 1, 10):
        break