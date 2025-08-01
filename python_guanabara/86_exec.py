matriz = [[0,0,0],[0,0,0],[0,0,0]]
spr = maior = co =0
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a matriz [{linha},{coluna}]'))
        
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]}]', end='')
        if matriz[l][c] % 2 == 0:
            spr += matriz[l][c]
    print()
print(spr)
for l in range(3):
    co += matriz[l][2]
print(co)
print(max(matriz[1]))