limite_credito = 900
total_compras = 325.56
saldo_disponivel = limite_credito - total_compras

valor_compra = float(input("Informe o valor da compra: "))

if valor_compra <= saldo_disponivel:
    saldo_disponivel = saldo_disponivel - valor_compra
    print("Sua compra foi autorizada.\n"
          f"Valor da compra: R$ {valor_compra:.2f}\n"
          f"Seu saldo atualizado é: {saldo_disponivel:.2f}")
else:
    print("Sua compra não foi autorizada.\n"
          "Saldo insuficiente.\n"
          f"Saldo disponível: R$ {saldo_disponivel:.2f}")