def funcao_externa():
    b = 20
    global a
    a = 80
    print(f"Imprimindo 'b' em funcao_externa: {b}")
    print(f"Imprimindo 'a' em funcao_externa: {a}")
    def funcao_interna():
        c = 30
        b = 25
        global a
        a = 70
        print(f"Imprimindo 'c' em funcao_interna: {c}")
        print(f"Imprimindo 'b' em funcao_interna: {b}")
        print(f"Imprimindo 'a' em funcao_interna: {a}")

    funcao_interna()
    print(f"Imprimindo 'b' de novo em funcao_externa: {b}")

a = 10

print(f"Imprimindo 'a' no escopo global: {a}")
funcao_externa()
print(f"Imprimindo 'a' de novo no escopo global: {a}")