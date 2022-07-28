

a=float(input('Digite um numero: '))
b=float(input('Digite outro número'))
c=float(input('Digite mais um número:'))


if a<b+c and b<a+c and c<a+b:
    print(f'Pode ser um triangulo',end='')
if a==b==c:
    print('Equilatero')
elif a!=b!=c!=a:
    print('Escaleno')
else:
    print('Isósceles')

