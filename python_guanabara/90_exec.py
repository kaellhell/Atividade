ficha =[]
aluno = {}

aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input(f'Media do {aluno["nome"]}: '))

if aluno['media'] >= 6:
   aluno['situação'] = 'aprovado'

else:
    aluno['situação'] = 'reprovado'

ficha.append(aluno.copy())

for elemento in ficha:
    for k,v in elemento.items():
        print(f'{k} é igual a {v}') 
