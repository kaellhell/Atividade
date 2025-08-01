lista = []

for c in range(1,6):
    numero = int(input('Digite um valor numerico: '))
    posição_encontrado = False

    for i, item in enumerate(lista):
        if numero <= item:
            lista.insert(i,numero)
            print(f'adicionado na posição {i} da lista')
            posição_encontrado = True
            break
           
    if not posição_encontrado:
                lista.append(numero)
                print(f'Adicionado no final da lista')
print(lista)