from random import randint
cont = 0
num = 0
alea = randint(0,5) 
while num != alea:
   cont += 1
   alea = randint(0,5) 
   num = int(input('escolha um numero de 0 a 5:\n'))
   if num == alea:
        
        print(f'parabens voce acertou o numero {alea} em {cont} tentativa!')
        
   elif num > 5 or num <0:
         print(f'condição invalida, escolha um numero de 0 a 5')
   else:
        print(f'voce errou o {alea}, tente novamente')  
       
