import datetime
ano_nascimento = int(input('Insira a sua data de nascimento:\n'))

dataAtualCompleto = datetime.date.today()

dataAtual = dataAtualCompleto.year
idade = dataAtual - ano_nascimento

print('idade do participande é ', idade)
print('\033[34m-=-\033[0m' * 10)

if idade <= 9:
    print('Sua categoria é \033[31m Mirin \033[0m')
elif idade < 14:
    print('Sua categori é \033[31m Infantil\033[0m')
elif idade < 19:
    print('Sua categoria é \033[31m junior\033[0m')
elif idade < 25:
    print('Sua categoria é \033[31m sênior\033[0m')
else:
    print('Sua categoria é \033[31m Master\033[0m')
print("\033[34m-=-\033[0m" * 10)

print("Bem-vindo")