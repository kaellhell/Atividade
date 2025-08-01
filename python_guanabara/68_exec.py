from random import randint
from time import sleep
cont = 0    
while True:
    computador = randint(1,10)
    print('=-' * 20)
    print('Vamaos jogar Par ou Impar!')
    print('=-' * 20)
    jogador = int(input('Digite um valor: '))
    tipo = input('Par ou Impar? [P/I] ').strip().upper()[0]
    total = computador + jogador
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR!' if total % 2 == 0 else 'DEU ÍMPAR!')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
        else:
            print('Você PERDEU!')
            break
            
    cont += 1 
    sleep(0.5)
print(f'Você vence ganhou {cont} vezes. Até mais!')