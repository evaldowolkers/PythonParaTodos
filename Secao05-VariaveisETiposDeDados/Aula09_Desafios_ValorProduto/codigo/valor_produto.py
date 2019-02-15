valor_parcela = float(input("Informe o valor da parcela mensal: "))
quantidade_meses = int(input("Informe a quantidade de meses: "))

valor_compra = valor_parcela * quantidade_meses

print(f"O valor da compra é: {valor_compra:,.2f}")
