name = input('Write your name:')

if (len(name) <4):
    print(f'{name} is a short name.')
elif (len(name)>=5 and len(name)):
    print(f'{name} is a length normal name.')
else:
    print(f'{name} is a long name.')