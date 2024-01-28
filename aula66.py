''' Calculadora com While '''

# Vou pedir dois numeros para um usuario e ele escolhera a operacao: +,-,*,/

while True:
    n1=input('Digite um numero: ')
    n2=input('Digite um numero: ')
    operacao=input('Selecione uma das operacoes: +,-,*,/: ')


    print(f'{n1}{operacao}{n2}= {eval(f"{float(n1)} {operacao} {float(n2)}")}')

    opcao=input('Voce quer sair ? [s]im: ').lower().startswith('s') # Usuario recebe um valor que independente de ser maiusculo, ou minusculo 
                                                                                # o valor e alterado para minusculo, depois a funcao verifica se a o valor digitado
                                                                                # inicia com 's'
    if opcao == True:
        break
