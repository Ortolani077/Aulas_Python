import math

a=float(input('Digite um numero: '))
b=float(input('Digite outro número'))
c=float(input('Digite mais um número:'))
tri=a+b+c

if a+b>c or b+c>a or a+c>b:
    print(f'Pode ser um triangulo')
else:
    print('Não é')