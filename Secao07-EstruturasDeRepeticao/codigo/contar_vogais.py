palavra = input("Digite uma palavra: ")
a = 0
e = 0
i = 0
o = 0
u = 0

for letra in palavra:
    if letra.lower() == 'a':
        a += 1
    elif letra.lower() == 'e':
        e += 1
    elif letra.lower() == 'i':
        i += 1
    elif letra.lower() == 'o':
        o += 1
    elif letra.lower() == 'u':
        u += 1

print(f"Qtd. de 'a': {a}")
print(f"Qtd. de 'e': {e}")
print(f"Qtd. de 'i': {i}")
print(f"Qtd. de 'o': {o}")
print(f"Qtd. de 'u': {u}")
