from time import sleep
while True:
    num = int(input('Digite um númeropara ver sua tabuada (numero negativo para parar): '))
    if num < 0:
        print('encerrando...')
        break   
    print(f'Tabuada do {num}:')
    print('-' * 20)
    for i in range(1,11):
        sleep(0.2)
        print(f'{num} x {i} = {num * i}')
    print('^~' * 20)