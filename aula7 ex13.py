n1=float(input(' Digite o valor do salário: R$'))
por=float(input('Digite o percentual de aumento:'))
aum1=float(n1//100)
aum2=float(aum1*por)
aum3=float(aum2+n1)

print(f' O salário com' ,por, '% de aumento passará a ser R$',  aum3)