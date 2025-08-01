from random import randint
from time import sleep
lista = []

def sortea(adc):
    print(f'sorteando 5 valores da lista' )
    for v in range(5):
        v = randint(0,10)
        adc.append(v)
        print(f'{v}',end=' ', flush=True)
        sleep(0.5)
    print('PRONTO!!')


def somapares(pares):
    soma =0 
    for s in pares:
        if s%2 == 0:
            soma += s
    print(f'A soma dos pares da lista {lista} é {soma}')

sortea(lista)
somapares(lista)
