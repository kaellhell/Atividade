num = int(input('Digite um número para ver a sequência de Fibonacci até ele:'))
t1 = 0
t2 = 1
cont = 0
print(f'{t1} -> {t2} -> ', end='')
while cont != num:
    proximo_termo = t1 + t2
    print(f'{proximo_termo} -> ', end='')
    t1 = t2
    t2 = proximo_termo
    cont += 1
print(' FIM')
''