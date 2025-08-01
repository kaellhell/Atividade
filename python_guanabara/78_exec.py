valores=[]
mai = men =0
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
    if cont ==0:
        mai = men = valores[cont]
    else:
        if valores[cont] > mai:
            mai = valores[cont]
        if valores[cont] < men:
            men = valores[cont]

print(f'Você digitou os valores {valores}')
print(f'O maior número é {mai} nas posiçoes ', end=' ')
for i,v in enumerate(valores):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O menor número é {men} nas posiçoes ', end=' ')
for i, v in enumerate(valores):
    if v == men:
        print(f'{i}...', end='')
print()