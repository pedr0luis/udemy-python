hora = input('Digite a hora: ')
print(f'{int(hora[:2])} e {(type(int(hora[:2])))}')

try:
    if (int(hora[:2]) >= 0) or (int(hora[:2]) >+ 23):
        if int(hora[:2]) <= 11:
            print('Bom dia!')
        elif int(hora[:2]) >= 11 and int(hora[:2]) <= 17:
            print('Boa tarde!')
        else:
            print('Boa noite!')
    else:
        print('Valor digitado nao esta entre [0-23].')
except:
    print('Valor digitado nao e numero.')