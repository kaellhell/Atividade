num = int(input('Digite um número: '))
c = num
print(f'Calculando {num}! = ', end='')
f = 1
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c> 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')