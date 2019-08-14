estoque = { "1": ["Teclado", 300, 166.71],
            "2": ["Mouse", 125, 80.57],
            "3": ["Processador", 25, 875.64],
            "4": ["Cooler", 70, 35.14]}

print(f"Estoque atual:")
print("Código - Descrição - Qtd. - Valor Unitário")
for codigo in estoque:
    print(codigo, ' - ', estoque[codigo][0], ' - ', estoque[codigo][1], ' - ', estoque[codigo][2])

while True:
    acao = input("Informe a opção desejada. \n"
                 "1: Registrar entrada de produto\n"
                 "2: Registrar saída de produto\n"
                 "3: Sair do sistema: ")

    if acao == "3":
        break
    else:
        codigo = input("Informe o código do produto: ")

        if acao == "1":
            qtd = int(input("Informe a quantidade de entrada do produto: "))
            estoque[codigo][1] += qtd
        elif acao == "2":
            qtd = int(input("Informe a quantidade de saída do produto: "))
            if qtd <= estoque[codigo][1]:
                estoque[codigo][1] -= qtd
            else:
                print("Quantidade insuficiente em estoque!!!")

print("Estoque atualizado:")
print("Código - Descrição - Qtd. - Valor Unitário")
for codigo in estoque:
    print(codigo, ' - ', estoque[codigo][0], ' - ', estoque[codigo][1], ' - ', estoque[codigo][2])
