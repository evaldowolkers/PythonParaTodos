lista1 = [10, 25, 37]
lista2 = [42, 18, 74]

soma = map(lambda x, y: x+y, lista1, lista2)
for n in soma:
    print(n)