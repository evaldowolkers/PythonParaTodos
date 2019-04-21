def teste_escopo():
    def escopo_local():
        variavel = "escopo local"
        print("Dentro de escopo_local: ", variavel)

    def escopo_nonlocal():
        nonlocal variavel
        variavel = "escopo nonlocal"

    def escopo_global():
        global variavel
        variavel = "escopo global"

    variavel = "teste escopo"
    escopo_local()

    #Aqui é impressa a variável de dentro da função teste_escopo
    # e não a variável de dentro da função escopo_local
    print("Após atribuição local:", variavel)

    # non_local altera a variável da teste_escopo
    escopo_nonlocal()
    print("Após atribuição non_local:", variavel)

    # global não altera a variável dentro de teste_escopo
    # altera somente no escopo local, será impresso aqui a variável
    # de escopo non_local
    escopo_global()
    print("Após atribuição global:", variavel)

teste_escopo()
# Aqui está sendo impressa a variável no escopo global
print("Em escopo global:", variavel)