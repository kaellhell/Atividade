#escreva um programa para aprova um emprestimo bancario para compra uma casa
#o Programa vai pergunta o valor da casa, o salario do comprado e em quanto anos ele vai pogar
#calcule o valor da prestação mensal. sabendo que não pode exerce 30% do valor do salario
# ou entao o emprestimo sera negado.
print("-=-" * 20)
valorImovel  = float(input('Digite o valor do imovel:\nR$'))
salario = float(input('Informe o seu salario:\nR$'))
ano = int(input('enquando anos deseja pagar?\n'))
print("-=-" * 20)
qts = ano * 12 
parcelas = valorImovel / qts
restricao = salario * 0.30
if parcelas >= restricao:
    print('Seu emprestimo foi negado')
else:
    print('Emprestimo Apravado')
    print("-" * 20)
    print('valor do imovel: R${}'.format(valorImovel))
    print('parcelas: ', qts)
    print('valor da prestação: R${:.2f}'.format(parcelas))