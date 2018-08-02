def validar_tamanho(texto, maximo):
    if len(texto) > maximo:
        print(f"O texto deve conter no máximo {maximo} caracteres!")
    else:
        return True

while True:
    texto = input("Informe um texto de no máximo 20 caracteres: ")
    if validar_tamanho(texto, 20):
        break


