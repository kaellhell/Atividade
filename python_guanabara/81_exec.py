lista = []
num =0
while True:
    num = int(input('Digite um valor: '))
    if num < 0:
        break
    lista.append(num)

print(lista)
print(f'Quando numeor foram digitados: {len(lista)}')
lista.sort(reverse=True)
print(f'Lista em Descrecende {lista}')
if 5 in lista:
    print('Sim, valor cinto esta na lista.')
else: 
    print('o valor 5 não esta na lista.')