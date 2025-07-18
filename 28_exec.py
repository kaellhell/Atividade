#crier um programa que sorteie um numero de 0 a 5 e peça para o usuario tentar adivinhar
#se o usuario acertar, mostrar uma mensagem de parabens, se errar, mostrar
# random faz uma escolha aleatoria de um numero inteiro
#e o randint escolhe um numero inteiro entre dois valores
from random import randint
# time é usado para fazer uma pausa no programa
#sleep faz o programa esperar um tempo antes de continuar
from time import sleep
#inseri o resultado do sorteio na variavel alea
alea = randint(0,5)

num = int(input('escolha um numero de 0 a 5:\n'))
#verifica se o numero digitado pelo usuario é igual ao sorteado
#se for igual, mostra uma mensagem de parabens, se não, mostra uma mensagem de erro
print('Processando...')
sleep(2)  # Pausa de 2 segundos para simular processamento
if num == alea:
    print(f'parabens voce acertou o numero {alea}!')
elif num > 5 or num <0:
    print(f'condição invalida, escolha um numero de 0 a 5')
else:
    print(f'voce errou o {alea}, tente novamente')