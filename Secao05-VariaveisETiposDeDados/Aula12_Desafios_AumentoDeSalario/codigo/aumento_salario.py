salario_atual = float(input("Informe o salário atual: "))
percentual_aumento = float(input("Informe o percentual de aumento: "))

novo_salario = salario_atual + (salario_atual * (percentual_aumento / 100))
print(f"O valor do salário atualizado é: {novo_salario:,.2f}")