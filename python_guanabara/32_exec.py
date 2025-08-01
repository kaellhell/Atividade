#faça um program que leio o anos e mostre se ele é bissexto ou não
ano = int(input('digite um ano:\n'))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'o ano é {ano} é bissexto')
else:
    print('o ano {ano} não é bissexto')