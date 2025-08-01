def ficha(p = 'desconhecido',g = 0):
    print(f'o Jogador {p} fez {g} no campeonato.')
    


jogador=str(input('Nome do jogador: '))
gol = str(input('Numero de gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol =0
if jogador.strip() == '':
    ficha(g=gol)
else:
    ficha(jogador, gol)
