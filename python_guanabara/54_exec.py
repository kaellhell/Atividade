from datetime import date
maior = 0
menor = 0
data_atual = date.today().year
for c in range(8):
    n = int(input('insira a data de nascimento do {}:\n'.format(c)))

    idade = data_atual - n

    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(' \033[31m {}\033[0m são maiores de idade\ne \033[31m{}\033[0m são menores de idade'.format(maior,menor))