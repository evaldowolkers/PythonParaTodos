"""
05) Crie um programa que solicite ao usuário que informe o valor
de seu salário, o valor do salário mínimo e sua idade.
Compare se o valor do salário é maior que dois salários
mínimos E se a idade informada é maior que 18 usando operadores
lógicos e relacionais. Imprima no final: "O resultado foi X",
sendo que X será "True" ou "False".
"""
salario = float(input("Informe o valor do seu salário: "))
salario_minimo = float(input("Informe o valor do salário mínimo: "))
idade = int(input("Informe sua idade (apenas número): "))
resultado = salario > (salario_minimo * 2) and idade > 18
print("O resultado foi", resultado)