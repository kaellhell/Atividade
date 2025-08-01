lista = []
for c in range(5):
    peso = float(input('insira o peso:\n'))
    lista.append(peso)
print('\033[31m-=-\033[0m' * 20)
if max(lista) >= 50 and max(lista) < 70:
        print('maior peso:', max(lista))
        print('peso normal')
elif max(lista)>= 70 and max(lista) < 90:
        print('maior peso:', max(lista))
        print('sobrepeso')
elif max(lista) >= 90:
        print('maior peso:', max(lista))
        print('obesidade') 
else:
        print('maior peso:', max(lista))
        print('abaixo do peso')

if min(lista) >= 50 and min(lista) < 70:
    print('menor peso:', min(lista))
    print('peso normal')
elif min(lista)>= 70 and min(lista) < 90:
    print('menor peso:', min(lista))
    print('sobrepeso')
elif min(lista) >= 90:
    print('menor peso:', min(lista))
    print('obesidade') 
else:
    print('maior peso:', min(lista))
    print('abaixo do peso')