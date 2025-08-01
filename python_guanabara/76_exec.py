listagem = ('pão', 2, 'leite', 3.5, 'ovo', 12, 'arroz', 5.99,
            'feijão', 7.45, 'macarrão', 4.99, 'carne', 25.99,
            'frango', 19.99, 'batata', 3.49,'tomate', 2.99,)
print('-'*40)
print(f'{"LISTAGEM DE PRODUTOS":^40}')  
print('-'*43,)
for pos in range(0, len(listagem)):
    if pos % 2 ==0:
        print(f'|{listagem[pos]:.<30}', end=' ')
    else:
        print(f'R${listagem[pos]:>7.2f}',' |')
print('-'*43)
   
    