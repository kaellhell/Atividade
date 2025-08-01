valores = []
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont:}: ')))

for c, v in enumerate(valores):
    print(f'\n8Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista.')