palavra = 'arara'
letra_acertadas = ''

while True:
    letra_digitada = input('Digite uma letra_digitada:').lower()
    if len(letra_digitada) > 1 or letra_digitada == ' ':
        print(f'Valor digitado invalido! Digite uma letra_digitada.')
        continue
    if letra_digitada in palavra:
        letra_acertadas += letra_digitada
    else:
        adivinhe[c]='*'
    print(f'adivinhe')
