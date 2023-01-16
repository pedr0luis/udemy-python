nome = input('Digite seu nome: ')
idade = input(f'{nome} digite sua idade: ')

if len(idade)>0 and len(nome)>0:
    print(f'Seu nome e {nome}')
    print(f'{nome} esse e seu nome invertido {nome[::-1]}')
    if ' ' in nome:
        print('Ha espacos no seu nome')
    else:
        print('Nao ha espacos no seu nome')
    espaco = 0
    for C in range (len(nome)):
        if nome[C] == ' ':
            espaco = espaco + 1
    print(f'Ha {espaco} espaco em seu nome')
    print(f'Seu nome tem {len(nome)-espaco} letras')
    print(f'A primeira letra de seu nome e {nome[0]}')
    print(f'A ultima letra de seu nome e {nome[-1]}')
else:
    print('Desculpe, voce deixou campos vazios.')
        
