
salario=float(input('Digite o valor do salário R$ '))
alm2=(salario/100*15)
alm3=(salario / 100 * 10)
aumreal2 = alm3 + salario

aumreal=alm2+salario

if salario<= 1250:
    print(f'Seu aumento é de R$:', alm2, 'ficando com um salário total de R$', aumreal)

else:


    print(f'Seu aumento foi de R$', alm3, 'Ficando com um salário no total de R$', aumreal2)

