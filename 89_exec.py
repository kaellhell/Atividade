escola = []

while True:
    aluno=[]

    nome = str(input('Digite o Nome do aluno: ')).upper()
    aluno.append(nome)
    while True:

        nota=[]
        
        while True:
            nota1 = float(input('Digite a 1° nota do aluno: '))
            if nota1 >= 0 and nota1 <= 10:
               nota.append(nota1)
               break           
            else:
             print('Porfavor, Digite uma nota entre 0 á 10: ')

        while True:
            nota2 = float(input('Digite a 2° nota do aluno: '))
            if nota2 >=0 and nota2 <= 10:
               nota.append(nota2)
               break
            else: 
               print('Porfavor, Digite uma nota entre 0 á 10: ')

        media = (nota1+nota2)/2
        nota.append(media)
        break

    aluno.append(nota[:])
    escola.append(aluno[:])
    aluno.clear()

    resp = str(input(f'Adiciona outro aluno: \033[32m[S/N]\033[0m')).strip().upper()
    if resp in 'N':
        break
print('NO. NOME      MEDIA')
print('-'*25)
for cont, alunos in enumerate(escola):
    print(f'{cont}. {alunos[0]:<10}{alunos[1][2]:> 6}')

print('-'*25)
index = 0
while index != 999:
   index = int(input('Insira o codigo do aluno para vê a nota: '))
   print(escola[index][0],escola[index][1][0], escola[index][1][1])
   print('Digite 999 para encerra.')
   
print('Finalizando')