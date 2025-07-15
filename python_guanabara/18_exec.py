import math
a = float(input('Digite um valor do angulo para descobrir o seno, cos e a tajente: '))
rad = math.radians(a)
seno = math.sin(rad)
coseno = math.cos(rad)
tangente = math.tan(rad)
print(f"o seno de {a} é {seno:.2f}")
print(f"o cos de {a} é {coseno:.2f}")
print(f"o tangente de {a} é {tangente:.2f}")