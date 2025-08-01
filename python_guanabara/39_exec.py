#faça um programa que leia o ano de nascimento de um jovem e informe 
#de acordo com sua idade, se vai se alista, se ja esta na hora, ou ja passou da hora e quando dias falta para se alista
import datetime 
dataAtual = datetime.date.today()
    
ano = int(input('informe o seu ano de nascimento:\n'))
mes = int(input('informe o seu mes de nascimenro:\n'))
dia = int(input('informe o seu dia de nascimenro:\n'))
dataNascimento = datetime.date(ano,mes,dia)
idade = dataNascimento - dataAtual 

if dataNascimento.month < dataAtual.month or  (dataNascimento.year == dataAtual.year and dataNascimento.day - dataAtual.day):
    idade -=1
    
    print('Sua idade {}'.format(idade))

    idadeAlistamento = 18  

if idade < idadeAlistamento:    

    dataAlistamento = datetime.date(ano + idadeAlistamento,mes,dia)
    diasRestante = (dataAlistamento - dataAtual).days

    print(f"Você ainda vai se alistar. Faltam {diasRestante} dias para você completar {idadeAlistamento} anos.")
    print(f"Seu alistamento será a partir de {dataAlistamento.year}.")

elif idade == idadeAlistamento:

    print("É hora de se alistar! Você está na idade ideal para o alistamento militar.")
    print("Fique atento aos prazos do seu município.")
else:

    anoAtrasado = idade- idadeAlistamento

    print("Já passou da hora de se alistar!")
    print(f"Você está {anoAtrasado} ano(s) atrasado no alistamento.")