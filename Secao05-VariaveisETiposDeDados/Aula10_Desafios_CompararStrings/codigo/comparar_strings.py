texto1 = input("Informe o primeiro texto: ")
texto2 = input("Informe o segundo texto: ")

print("Texto 1: ", texto1)
print("Texto 2: ", texto2)

print(f"Quantidade de caracteres de '{texto1}': {len(texto1)}")
print(f"Quantidade de caracteres de '{texto2}': {len(texto2)}")

print("As strings possuem mesma quantidade de caracteres?", len(texto1) == len(texto2))
print("As strings são iguais?", texto1 == texto2)