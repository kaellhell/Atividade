def leiaInt(mgs):
    ok = False
    valor = 0

    while True:
        n = str(input(mgs))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[32m ERRO, Digite um numero valido.\033[0m')
        if ok:
            break
    return valor



n = leiaInt('Digite um numero: ')
print(f'O numero digita é {n}')