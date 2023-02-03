while True:
    valor_1 = input('Digite um valor: ')
    valor_2 = input('Digite um segundo valor: ')
    operador = input('Digite a operacao a ser feita (+-/*): ')
    try:
        if operador in '-+/*':
            if len(operador) == 1 and operador != ' ':
                if operador == '+':
                    print(f'{valor_1} {operador} {valor_2} = {float(valor_1) + float(valor_2)}')
                elif operador == '-':
                    print(f'{valor_1} {operador} {valor_2} = {float(valor_1) - float(valor_2)}')
                elif operador == '/':
                    print(f'{valor_1} {operador} {valor_2} = {float(valor_1) / float(valor_2)}')
                else:
                    print(f'{valor_1} {operador} {valor_2} = {float(valor_1) * float(valor_2)}')
            else:
                print('Digite um unico operador!')
        else:
            print('Digite um um operador valido!')
            continue
    except:
        print('Digite dois numeros')
        continue
    sair = input('Quer sair ? [s]im [n]ao: ').lower().startswith('s')
    if sair is True:
        print('sair')
        break
