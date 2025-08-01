lista = [[], []]

for c in range(0,7):
    num =int(input(f'Digite um valor na {c + 1}°: '))
    if c % 2 == 0:
        lista[0].append(num)
    else:   
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print(lista)
print(lista[0])
print(lista[1])