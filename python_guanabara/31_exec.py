#Desenvolva um progroma que pergubte a distancia de uma viagem em km.
#Calcule o preço da passagem cobrando R$0,50 por km rodado para viagens de até 200km
#e R$0,45 para viagens mais longas.
#  
distancia = float(input('qual a distancia da viagem em km?\n'))

#if distancia <= 200:
#   preco = distancia * 0.50
#else:
#    preco = distancia * 0.45

#simplificado 

preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'O valor da pasagem é R$: {preco:.2f}')