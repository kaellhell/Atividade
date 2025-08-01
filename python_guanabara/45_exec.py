import random
import time

player = int(input('escolhar uma opção Abaixo\n\033[31m1-Pedra\n2-Papel\n3-Tesoura\033[0m\n'))
comp = random.randint(1,3)
print('Processando..')
time.sleep(3)
if comp == 1:
    print('computador escolheu: Pedra')
elif comp == 2:
    print('computador escolheu: Papel')
else:
    print('computador escolheu: Tesoura')


if player == 1 and comp == 2:
    print('voçê perdeu!')
elif player == 2 and comp == 3:
    print('Voçê Pedeu!')
elif player == 3 and comp == 1:
    print('Voçê Pedeu!')

elif player == 3 and comp ==2:
    print('Parabéns voçê Ganhou!!')
elif player == 2 and comp == 1:
    print('parabéns voçê Ganhou!!')
elif player == 1 and comp == 3:
    print('parabéns voçê Ganhou!!')

elif (player == 1 and comp == 1) or (player == 2 and comp == 2) or (player == 3 and comp == 3):
    print('empatou!\nVamos de novo!!')
