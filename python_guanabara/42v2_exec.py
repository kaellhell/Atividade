lado1 = float(input('insira um valor:\n'))
lado2 = float(input('insira um segundo valor:\n'))
lado3 = float(input('insira um terceiro valor:\n'))

if lado1 == lado2 and lado2 == lado3:
    print('é \033[34mEquilâtero\033[0m')
elif (lado1 == lado2 and lado2 != lado3) or (
      lado1 == lado3 and lado1 != lado2) or (
      lado2 == lado3 and lado1 != lado2):
    print('é \033[34mIsósceles\033[0m')
elif lado1 != lado2 and lado2 != lado3:
    print('é \033[34m escaleno\033[0m')