"""
03) Crie um programa que solicite o ano de nascimento do
usuário (com 4 dígitos) e calcule sua idade
(tem que converter o ano para inteiro antes de calcular).
Imprima a frase:
"Você tem X anos.", onde "X" é a idade calculada.
Obs.: Utilizamos o ano 2019 fixo, mas você deve informar
o ano atual, caso esteja fazendo este exercício após 2019.
"""
ano_nascimento = int(input("Informe o ano de nascimento com "
                           "4 dígitos: "))
idade = 2019 - ano_nascimento
print("Você tem", idade, "anos.")