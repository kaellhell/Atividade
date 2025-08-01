valores = []
par = []
for c in range(4):
     valor = int(input(f'Digite um valor: '))
     
     valores.append(valor)
tuplas = tuple(valores)
for i in tuplas:
    if i % 2 == 0:
        par.append(i)
    

print(f'O valor 9 apareceu {(tuplas.count(9))} vez(es).')
print(f'O valor 3 apareceu na {tuplas.index(3)+1}° posição.' if 3 in tuplas 
      else 'o valor 3 não foi digitado.')
print(f'Os valores pares digitados foram: {par}'if par else 'Nenhum valor par foi digitado.')