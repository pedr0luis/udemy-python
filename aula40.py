nome = 'Giovani Teixeira'

tamanho_nome = len(nome)
contador = 0
nova_string=''

while contador < tamanho_nome:
    print(f'{nome[contador]}')
    nova_letra = '*'+nome[contador]
    if nome[contador] == ' ':
        nova_letra=''
    nova_string += nova_letra
    contador += 1
nova_string += '*'
print(f'{nova_string}')