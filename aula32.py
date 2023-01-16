numero_str = input('Digite um numero inteiro: ')

try:
    if (int(numero_str)%2 == 0):
        print(f'{numero_str} e um numero par.')
    else:
        print(f'{numero_str} e um numero impar.')
except:
    '''if numero_str in [a-z]:
        print('Voce diigtou um numero decimal')
    else:'''
    print('Voce nao digitou um numero')