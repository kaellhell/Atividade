from random import randint
tuplas = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'Os valores sorteandos foram: ', end='')
for i in tuplas:
    print(f'{i}', end=' ')
print(f'\nMaior valor sorteado foi {max(tuplas)}')
print(f'o menor valor sorteado foi {min(tuplas)}')