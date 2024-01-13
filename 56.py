hora,minuto = input('Digite a hora: ').split(':')
hora = int(hora)

if (hora >=0) and (hora <12):
    print('Bom dia!!')
elif (hora >= 12) and (hora <18):
    print('Boa tarde!')
elif (hora >23):
    print('Hora invalida')
else:
    print('Boa noite!')