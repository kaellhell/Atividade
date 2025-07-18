#crier um programa que leia duas nota do aluno e mostre a media
#e motres se ele reprovou, ficou de recuperação ou aprovou
nota1 = float(input('insira a primeira nota do aluno:\n'))
nota2 = float(input('insira a segunda nota do aluno:\n'))

media = (nota1 + nota2)/2
if media <=4.9:
    print('você reprovou, estude mais!')
elif media >= 5 and media <= 5.9:
    print('você ficou de recuperação\n continue se esforçando!')
else:
    print('parabéns você passou')