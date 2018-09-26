"""
3) Crie um programa que solicite os seguintes dados ao usuário:
Informe o nome do produto:
Informe o preço do produto:
Informe a quantidade de produtos:
Ao final, usando composição de strings (%) imprima:
O produto NOME custa VALOR, você comprou QUANTIDADE e vai pagar TOTAL.
Lembre-se de formatar os floats com duas decimais.
"""
produto = input("Informe o nome do produto: ")
preco = float(input("Informe o preço do produto: "))
quantidade = int(input("Informe a quantidade de produtos: "))
total = preco * quantidade
print("O produto %s custa %.2f, você comprou %d e vai pagar %.2f." % (produto, preco, quantidade, total))