'''nome = "Luiz"
idade = 23
formato = '{1} tem {0} anos'
print(formato.format(nome, idade))'''

operador = input('')
if operador in '-+/*':
    if len(operador) == 1 and operador != ' ':
        print('Funcionou')
    else:
        print('Digite um unico operador!')
else:
    print('Digite um operador valido')