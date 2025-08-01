somaIdade=0
maiorIdade = 0
nomevelhor =''
totmulher = 0
for c in range(1,5):
    print('---{}º PESSOA---'.format(c))
    nome = input('Digite o nome:\033[31m\n\033[0m')
    idade = int(input('Digite a idade:\033[31m\n\033[0m'))
    sexo = input('Digite o sexo:\033[31m\n\033[0m').strip().upper()
    somaIdade += idade
    
    if c == 1 and sexo in 'Mm':
        maiorIdade = idade
        nomeVelhor = nome
    if sexo in 'Mm' and idade > maiorIdade:
        maiorIdade = idade
        nomeVelhor = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1

mediaidade = somaIdade / 4
print('A media do grupo é de \033[31m{:.1f}\033[0m anos'.format(mediaidade))
print('Homem mais velhor é\033[31m {}\033[0m com \033[32m{} anos\033[0m'.format(nomeVelhor, maiorIdade))
print('Total de mulher com menos de 20 anos é\033[31m {}\033[0m'.format(totmulher))