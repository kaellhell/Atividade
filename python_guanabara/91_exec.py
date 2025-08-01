from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador 1º': randint(1,6),
        'jogador 2º': randint(1,6),
        'jogador 3º': randint(1,6),
        'jogador 4º': randint(1,6)}
ranking = []
print('Valores Sorteado: ')
for k,v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-'*30)
print(' RESULTADO: ')
for i,v in enumerate(ranking):
    print(f'{i+1}º o lugar:  {v[0]} com {v[1]}.')
    sleep(0.5)