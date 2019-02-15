palavra = input("Digite uma palavra: ")
vogais = ["a", "e", "i", "o", "u"]
contar_vogais = [0, 0, 0, 0, 0]

for letra in palavra:
    if letra.lower() in vogais:
        contador = 0
        while contador < 5:
            if letra.lower() == vogais[contador]:
                contar_vogais[contador] += 1
            contador += 1

print(f"Qtd. de 'a': {contar_vogais[0]}")
print(f"Qtd. de 'e': {contar_vogais[1]}")
print(f"Qtd. de 'i': {contar_vogais[2]}")
print(f"Qtd. de 'o': {contar_vogais[3]}")
print(f"Qtd. de 'u': {contar_vogais[4]}")
