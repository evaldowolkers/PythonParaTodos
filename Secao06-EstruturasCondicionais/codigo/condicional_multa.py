#Tabela de multas
#Velocidade                                  Valor da multa          pontos      Suspensão CNH
#Até 20% acima da máxima permitida           R$ 130,16               4
#de 20% até 50% acima  da máxima permitida   R$ 195,23               5
#Superior a 50% da máxima permitida          R$ 880,41               7           Sim

velocidade_permitida = int(input("Informe a velocidade permitida "
                                 "na via: "))
velocidade_veiculo = int(input("Informe a velocidade que você "
                               "passou no radar: "))

if velocidade_veiculo > velocidade_permitida:
    if velocidade_veiculo >= velocidade_permitida + (velocidade_permitida * (50/100)):
        valor_multa = 880.41
        pontos = 7
        suspensao = True
        descricao_multa = "Transitar em velocidade superior a " \
                          "50% da máxima permitida"
    elif velocidade_veiculo >= velocidade_permitida + (velocidade_permitida * (20 / 100)):
        valor_multa = 195.23
        pontos = 5
        suspensao = False
        descricao_multa = "Transitar em velocidade superior à " \
                          "máxima permitida em 20% até 50%"
    else:
        valor_multa = 130.16
        pontos = 4
        suspensao = False
        descricao_multa = "Transitar em velocidade superior à " \
                          "máxima permitida em até 20%"

    print(f"Você foi multado e perdeu {pontos} pontos.")
    if suspensao:
        print("Você teve a carteira suspensa.")
    print(f"O valor de sua multa é: R$ {valor_multa}")
    print(f"Motivo: {descricao_multa}")
else:
    print("Parabéns, você não foi multado.")