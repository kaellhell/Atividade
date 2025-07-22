# Exercicio 59 - Menu de Opções5
from time import sleep
# Crie um programa que leia dois valores e mostre um menu na tela:
print('\033[32m-=-\033[0m' * 20)
num = int(input('Digite um numero: '))
num1 = int(input('Digite outro numero: '))

menu = 0
while menu != 5:
    print('\033[32m-=-\033[0m' * 20)
    print(' escolha uma opção abaixo:')
    sleep(0.3)
    print('\033[32m[1]\033[0m somar')
    sleep(0.3)
    print('\033[32m[2]\033[0m multtiplicar')
    sleep(0.3)
    print('\033[32m[3]\033[0m maior')
    sleep(0.3)
    print('\033[32m[4]\033[0m novo número')
    sleep(0.3)
    print('\033[32m[5]\033[0m sair do programa')
    print('\033[32m-=-\033[0m' * 20)

    menu = int(input('Digite sua opção: '))
    if menu == 1:
        soma = num + num1
        print(f'A soma entre {num} e {num1} é igual a {soma}')
    elif menu == 2:
        mult = num * num1
        print(f'A multiplicação entre {num} e {num1} é igual a {mult}')
    elif menu == 3:
        if num > num1:
            print(f'o maior número é {num}')
        else:
            print(f'o número maior é {num1}')
    elif menu == 4:
        print('Digite os números novamente')
        num = int(input('Digite um numero: '))
        num1 = int(input('Digite outro numero: '))
    elif menu == 5:
        print('saindo do programa...')
    else:
        print('Opção inválida, tente novamente!')