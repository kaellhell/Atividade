import datetime 
cadastro ={}
dataAtual = datetime.datetime.now()
dataAno = dataAtual.year
print(dataAno)
cadastro['Nome'] = str(input('Nome: '))
DataNascimento= int(input('Data de nascimento: '))
cadastro['idade'] =  dataAno - DataNascimento
cadastro['CPTS'] = int(input('CPTS: '))
if cadastro['CPTS'] != 0:
    cadastro['contratação'] = int(input('contratação: '))
    cadastro['salario R$']= float(input('Salario: '))
    cadastro['Aposentadoria'] = cadastro['idade'] + ((cadastro['contratação'] + 35) - dataAtual.year)

print('= = = DADOS PESSOAL = = =')
for k,v in cadastro.items():
    print(f'{k:<7} tem o valor {v:>7}.')