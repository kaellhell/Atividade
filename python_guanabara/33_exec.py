#crier uma programa que leia 3 numeros e mostre qual é o maior
#e se eles são iguais ou não
lista = []
num1 = int(input('digiti um numero1:\n'))
num2 = int(input('digite um numeor2:\n'))
num3 = int(input('digite um numero3:\n'))

lista.append(num1)
lista.append(num2)
lista.append(num3)

print(f'os numeros digitados foram: {lista}')
if num1 > num2 and num1 > num3 and num2 > num3:
    print(f'o numero {num1} é maior e o numero {num3} é o menor')
elif num2 > num1 and num2 > num3 and num3 > num1:
    print(f'o numero {num2} é maior e o numero{num1} é o menor')
elif num3 > num1 and num3 > num2 and num2 > num1:
    print(f'o numero {num3} é maior e o numero {num1} é o menor')
elif num1 > num2 and num1 > num3 and num3 > num2:
    print(f'o numero {num1} é maior e o numero {num2} é o menor')
else:
   print('os numeros são iguais')  

#---- Simplifincando -----#
# verificando o menor valor
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
#verificando o maior valor
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print('o maior valor é {}'.format(maior))
print('o menor valor é {}'.format(menor))