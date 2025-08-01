fichario = []
resp = ''
soma = media =0
while resp != 'N':
    cadastro = {}
    cadastro['nome'] = str(input('Nome: '))
    while True:
        cadastro['sexo'] = str(input('Sexo: ')).strip().upper()[0]
        if cadastro['sexo'] in 'MF':
            break
        print('ERRO, DIGITE O SEXO M OU F')
    cadastro['idade'] = int(input('Idade: '))
    soma += cadastro['idade']
    fichario.append(cadastro)
    resp = str(input('Deseja continua [S/N]')).strip().upper()
    
print('--Dados do fichario--')
print(f'N. de pessoas cadastrada: {len(fichario)}')
media = soma/len(fichario)
print(f'A média das idade é {media:.2f}')
print(f'N. Mulheres cadastrada:', end=' ')
for mulheres in fichario:
    if mulheres['sexo'] in 'Ff':
         print(f"{mulheres['nome']},", end=' ')
print()
print(f'Homens com  idade acima da media', end=' ')         
for p in fichario:
    if p['idade'] >= media and p['sexo'] == 'M':
        print(f'{p['nome']},')
print()
