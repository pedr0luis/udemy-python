nome =  input('Digite seu nome: ')

if len(nome) >1:
    if len(nome) <= 4:
        print(f'{nome} seu nome e curto')
    elif len(nome)>6:
        print(f'{nome} seu nome e muito grande')
    else:
        print(f'{nome} seu nome e normal')
else:
    print('Digite pelo menos uma letra')