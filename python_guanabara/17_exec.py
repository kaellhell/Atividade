import math
a = float(input('Digite um valor da cateto oposto: '))
b = float(input('Digite um valor da cateto adjacente: '))

c = math.hypot(a,b)
print(f'A hipotenusa vai medir {c:.2f}')