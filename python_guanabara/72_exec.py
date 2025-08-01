número = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    escolha = int(input('Digite um número entre 0 e 20: '))
    if 0 <= escolha <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você escolheu o número {número[escolha]}.')
