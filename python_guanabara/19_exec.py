import random 
lista_name = []

for i in range(4):
    name = str(input("digite o nome do aluno: \n"))
    lista_name.append(name)
sorteio = random.choice(lista_name)

print("-" * 40)
print("O aluno sorteado foi: ")
print(sorteio)

random.shuffle(lista_name)

print("-" * 40)
print("ordem de apresentação: ")
print(lista_name)

