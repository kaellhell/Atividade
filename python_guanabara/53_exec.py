frase = input('escreva uma frase:\n')
frase = frase.replace(' ','')
cont_frase = frase[::-1]
if frase == cont_frase:
    print("a frase é {} palindromo".format(frase))
    print('frase ao contrario é {}'.format(cont_frase))
else:
    print('a frase {} não é palindromo'.format(cont_frase))