def maior(*num):
    print('+'*len(num))
    print(f'{num} foram informado {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {max(num)}!')
    print('+'*len(num))
maior(4,5,6,2,78,6,4,1,)
maior(12,46,67,1)
maior(6)
maior()
