#crier um progrma que leia um numeor inteiro e mostre se ele é par ou impar
num = int(input('Digite um numero inteiro:\n'))
if num % 2 == 0:
    print('o numero {} é par'.format(num))
else:
    print('O numero {} é imper'.format(num))