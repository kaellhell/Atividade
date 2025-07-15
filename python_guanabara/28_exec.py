from random import choice
alea = [0,1,2,3,4,5]
sorte = choice(alea)
num = int(input('escolha um numero de 0 a 5:\n'))
if num == sorte:
    print(f'parabens voce acertou o numero {sorte}')
elif num > 5 or num <0:
    print(f'condição invalida, escolha um numero de 0 a 5')
else:
    print(f'voce errou o {sorte}, tente novamente')