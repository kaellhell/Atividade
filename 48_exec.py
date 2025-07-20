soma =0
conta =0
for c in range(1,501):
  if c % 3 == 0 and c % 2 != 0:
    soma += c
    conta = conta + 1

print('soma total de {} impares é {}'.format(conta,soma))