from random import randint
total = []

rodadas = int(input('Digite o numero de rodadas: '))

for s in range(rodadas):
    lista_atual = []
    for v,c in enumerate(range(6)):
        jogos = randint(1,61)
        if len(lista_atual) == 0:
            lista_atual.append(jogos)
        else:
            if lista_atual[v-1] != jogos:
                lista_atual.append(jogos)
    lista_atual.sort()
    total.append(lista_atual)
for i,s in enumerate(total):
    print(f'Jogo {i+1}: {s}')

    