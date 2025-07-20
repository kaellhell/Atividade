'''faça um progrrma que faça um contagem regressiva. de 
10 até 0'''
from time import sleep
tempo= int(input('insira o tempo da contagem:\n'))
print("")
for s in range(tempo):
    tempo -= 1
    sleep(1)
    print(tempo)
print('fogos de artificios:')