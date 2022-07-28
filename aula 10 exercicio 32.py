
ano=int(input('Qual ano estamos? '))
if (ano%400)==0 or (ano%4)==0 and(ano%100)!=0:
    print(f'Esse ano é bisesto')
else:
    print(f'Esse ano não é bisesto')


