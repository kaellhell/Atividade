#desenvolva um rpograma que leias o comprimento de 3 retas 
#e diga ao usuario se elas podem ou nao formar um triangulo
a = float(input('Digite o comprimnento da primeira reta:\n'))
b = float(input('Digite o comprimento de segunda reta:\n'))
c = float(input('Digite o comprimento da terceira reta:\n'))

if a < b + c and b < a + c and c < b + a:
    print('as retas podem formar uma tiangulo')
else:
    print('as retas nao podem formar um triangulo')