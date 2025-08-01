lista = []
par = []
impar = []

while True:
    num = int(input('Digite um valor: '))
    if num <=0:
        break
    lista.append(num)
print(lista)
for c, item in enumerate(lista):
    if item % 2 == 0:
        par.append(item)
    else:
        impar.append(item)
print(f'Par é {par}')
print(f'Impar é {impar}')