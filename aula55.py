
entrada = input('Digite um numero: ')

if entrada.isdigit():
    entrada = int(entrada)
    if (entrada % 2 == 0):
        print(f'{entrada} e um numero par.')
    else:
        print(f'{entrada} e um numero impar.')
else:
    print(f'{entrada} nao e um numero.')