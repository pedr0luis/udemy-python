primeiro_valor = input('Digite um valor:')
segundo_valor = input('Digite outro valor:')


if int(primeiro_valor) > int(segundo_valor):
    print(f'{primeiro_valor} > {segundo_valor}')
elif int(primeiro_valor) > int(segundo_valor):
    print(f'{segundo_valor} > {primeiro_valor}')
else:
     print(f'{segundo_valor} = {primeiro_valor}')
