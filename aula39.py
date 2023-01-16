nome  = input ('Digite seu nome: ')

c=0
nova_str = ''

if len(nome)>1:
    while c < len(nome):
        nova_str += f'*{nome[c]}'
        c +=1
    print(nova_str)
else:
    print('Digite uma letra pelo menos.')