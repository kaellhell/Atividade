c_idade = c_homem = c_mulher = 0 
while True:
    print('\033[34m---- Dados Pessoais ----\033[0m')
    idade = int(input('Digite a sua idade: '))
    sexo = input('Digite o seu sexo (M/F): ').strip().upper()
    if sexo not in 'MF':
        print('\033[31mSexo inválido! Por favor, digite M ou F.\033[0m')
        continue
    resp = input('você deseja continuar? \033[32m(S/N)\033[0m: ').strip().upper()
    
    if sexo == 'M':
        c_homem += 1

    if sexo == 'F' and idade < 20:
        c_mulher += 1

    if idade > 18:
        c_idade += 1 
    print('------------------------')
    if resp == 'N':
        break   
   
print(f'Total de pessoas cadastrada com  mais de 18 anos: {c_idade}')
print(f'Quandos homem foram cadastrados: {c_homem}')
print(f'Quantas mulheres tem menos de 20 anos: {c_mulher}')