lista = []
valores = 0
while valores >= 0:
    valores = int(input('Digite Um valor: '))
    if valores == -1:
        break
    if valores in lista:
        print('Valor ja foi adicionado')
    else:    
        lista.append((valores))
    lista_organizada = sorted(lista)
print(lista_organizada)