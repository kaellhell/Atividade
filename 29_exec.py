#escreve um programa que escre a velocidade de um carro
#se ele ultrapassar 80km/h mostre uma mensagem dizendo que foi multado 
#e o valor da multa, sendo R$7,00 por cada km acima do limite

vel = float(input('velocidade do veiculo:\n'))
if vel > 80:
    multa =(vel - 80) * 7
    print("vocé foi multado em R$ {:.2f} por excesso de velocidade".format(multa))