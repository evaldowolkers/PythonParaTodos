n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o segundo número: "))

resp = float(input(f"Informe o resultado da operação: {n1} + {n2} = "))
if resp == n1 + n2:
    print("Você acertou!!!")
else:
    print(f"Você errou. O resultado correto de {n1} + {n2} é: {n1 + n2}")

resp = float(input(f"Informe o resultado da operação: {n1} - {n2} = "))
if resp == n1 - n2:
    print("Você acertou!!!")
else:
    print(f"Você errou. O resultado correto de {n1} - {n2} é: {n1 - n2}")

resp = float(input(f"Informe o resultado da operação: {n1} * {n2} = "))
if resp == n1 * n2:
    print("Você acertou!!!")
else:
    print(f"Você errou. O resultado correto de {n1} * {n2} é: {n1 * n2}")

resp = float(input(f"Informe o resultado da operação: {n1} / {n2} = "))
if resp == n1 / n2:
    print("Você acertou!!!")
else:
    print(f"Você errou. O resultado correto de {n1} / {n2} é: {n1 / n2}")

