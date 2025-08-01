dados = []
pessoas =[]
mai = []
men = []
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(int(input('Peso: ')))
   
    if len(dados) == 0:
        mai = men = pessoas[1]
    else:
        if pessoas[1] > mai:
            mai = pessoas[1]
        if pessoas[1] < men:
            men = pessoas[1]
    dados.append(pessoas[:])
    pessoas.clear()

    res = str(input('Continuar \033[32m[S/N]\033[0m'))
    if res in 'Nn':
        break

print(f'{len(dados)} Foram cadastrada ')

print(f'As pessoais com {mai} KG são:', end='')
for p in dados:
    if p[1] >= 100:
        print(f'{p[0]}..', end='')
print('')

print(f'As pessoais com {men} KG são:', end='')
for p in dados:
    if p[1] <= 60:
        print(f'{p[0]}..', end='')
print('')