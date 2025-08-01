total =  c_preco = meno =0
while True:
    protudo = str(input('Nome do produto: ')).strip()
    preco = float(input('preço: R$ '))
    resp = str(input('Você deseja continuar? [\033[32mS\033[0m\033[31m/N\033[0m ')).strip().upper()
    print('------------------------')
    total += preco
    if preco > 1000:
        c_preco = 1
    if c_preco == 0:
        meno = preco
        nome = protudo
    if preco < meno: 
         meno = preco
         nome = protudo
    if resp == 'N':
        break
print(f'Total a pagar: R$ \033[31m{total:.2f}\033[0m')
print(f'Produtos que custam mais de R$ 1000: {c_preco}')
print(f'O produto mais barato foi \033[32m{nome}\033[0m e custa R$ \033[31m{meno:.2f}\033[0m')