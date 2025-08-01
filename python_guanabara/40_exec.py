#crier um programa que leia duas nota do aluno e mostre a media
#e motres se ele reprovou, ficou de recuperação ou aprovou
nota1 = float(input('insira a primeira nota do aluno:\n'))
nota2 = float(input('insira a segunda nota do aluno:\n'))

media = (nota1 + nota2)/2
if media <=4.9:
    print('você \033[31mreprovou\033[0m, estude mais!')
elif media >= 5 and media <= 5.9:
    print('você ficou de \033[34mrecuperação\033[0m\n continue se esforçando!')
else:
    print('\033[32mparabéns\033[0m você passou')