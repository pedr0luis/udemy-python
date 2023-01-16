numero_str = input('Digite um valor para eu dobrar: ')
try:
    print(f'O dobro de {numero_str} e {((float(numero_str))*2)}')
except:
    print('Isso nao e um numero')