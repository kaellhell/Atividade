lista =[]
soma = 0 
cont = 0
for c in range(6):
    n = int(input('insira um numero:\n'))
    if n % 2 == 0:
        soma += n
        cont += 1
        lista.append(n)
print(lista)
print(f'A soma dos {lista} é {soma} e a quantidade de numeros pares é {cont}.')