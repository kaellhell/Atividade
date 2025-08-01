sexo = ' '
while sexo not in 'MF':
    sexo = str(input('Informer o sexo [M/F]: ')).strip().upper()[0]
    if sexo not in 'MF':
        print('Dados inválidos. Por favor, informe M ou F.')
 
   
print(f'Sexo {sexo} registrado com sucesso.')    