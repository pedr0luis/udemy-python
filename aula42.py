frase = 'O Python e uma linguagem de programacao multiparadigma'\
    'Python foi criado por Guido van Rossum'.lower()

qnt_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

for c in range (len(frase)):
    if frase[c] == ' ':
        c += 1
        continue

    qnt_apareceu_mais_vezes_atual = frase.count(frase[c])

    if qnt_apareceu_mais_vezes < qnt_apareceu_mais_vezes_atual:
        qnt_apareceu_mais_vezes = qnt_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = frase[c]

print(f'A letra que mais apareceu foi "{letra_apareceu_mais_vezes}"'
f' que apareceu {qnt_apareceu_mais_vezes} x.')