somar = 0
final = 999
num = 0
while num != final:
    num = int(input('Digite um número [999 para parar]: '))
    if num == final:
        break
    somar += num
print('A somar dos valores foi {}'.format(somar))
  