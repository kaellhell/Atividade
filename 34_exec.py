#crier uma programa que calculer o reajuste salarial de um funcionario
#Ele deve receber o salario atual e o percentual de aumento 
#para salario superior a 1250,00 o aumento sera de 10%
#para salarios inferiores ou iguais a 1250,00 o aumento sera de 15%
salario = float(input('insira o salario atual: '))
if salario > 1250:
    aumento = salario *0.10
else:
    aumento = salario * 0.15
novo_salario = salario + aumento
print(f'O salario atual é {salario:.2f}\n e o novo salario é {novo_salario:.2f}\n com um aumento de {aumento:.2f}') 