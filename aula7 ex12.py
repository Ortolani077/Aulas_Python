n1=float(input('Digite o valor do produto:'))
n2=float(input('Digite a porcentagem do desconto'))
desc=float( n1/100)
desc2=float(desc*n2)
descfinal=float(n1-desc2)
print(f'O valor do produto será R$', descfinal, 'com', n2, '% de desconto' )
