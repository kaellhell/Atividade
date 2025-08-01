somar = maior = menor = media = cont =0
descisao = ''
while descisao != 'N':
    print('==--=='* 15)
    num = int(input('Digite o valor para saber  a media e o maior e menor valor: '))
    print('^^' *
           15)
    if cont == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    somar += num
    cont += 1
    descisao = input('Deseja continuar? \033[34m[S/N]\033[0m').strip().upper()[0]
    print(' ')
media = somar / cont
print('==--=='* 15)
print(f'A Media  dos valores é {media}, o mairo valor é {maior} e o menor valor é {menor}') 
