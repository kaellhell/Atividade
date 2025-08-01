lista = []
exp = input('digite: ')
for simp in exp:
    if simp == '(':
        lista.append('(')
    elif simp == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Expressão válida')
else:
    print('Expressão invalida')