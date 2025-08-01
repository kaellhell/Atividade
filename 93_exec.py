Fichario = []
resp= opcao =''
while resp != "N":
    soma=c = 0
    jogador = {}

    jogador['name'] = str(input('Nome do jogador: '))
    
    qts= int(input(f'Quantas partidas o jogador {jogador["name"]}: '))
    gols =[]

    for index in range(qts):
        gol = int(input(f'Quantos gols fez na partida {index+1}: '))
        gols.append(gol)
        soma += gol

    jogador['gols'] = gols
    jogador['Total'] = soma

    Fichario.append(jogador)

    resp = str(input('Deseja continua [S/N]')).strip().upper()

print('=-' * 30)
print(f'{"COD.":<5} {"NOME":<15} {"GOLS":<20} {"TOTAL":>7}')
print('=-' * 30)
for cod, jogodor_atual in enumerate(Fichario):
        print(f"{cod:<5}{jogodor_atual['name']:<10} {str(jogodor_atual['gols']):>10} {jogodor_atual['Total']:>15}")
while True:
    opcao = int(input('Digite um numero para ver redimento do JOgadores. (999 para sair)'))
    if opcao < len(Fichario):
        print(Fichario[opcao])
    elif opcao == 999:
         break
    else:
        print(f'Codigo invalido, Digite novamente.')



