from time import sleep
def contado(i, f, p):
    print('~~' * 20)
    print(f'Contador de {i} até {f} de {p} em {p}')
    sleep(1)
    if p == 0:
        p = 1
    if p < 0:
        p =1
    if i < f:
        cont = i
        while cont <=f:
            print(f'{cont}',end=' ', flush=True)
            cont += p
            sleep(0.5)
        print('FIM')

    elif i > f:
        cont =i
        while cont >= f:
            print(f'{cont}', end=" ", flush= True)
            cont -=p
            sleep(0.5)
        print("FIM")

                
inicio= int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contado(inicio, fim, passo)