import math

velocidade=float(input('Digite a velocidade do carro: '))
multa=(velocidade-80)
mult2=(multa*7)
if velocidade>80:
    print(f'Você foi multado em: R$', mult2 )
else:
    print(f'Sua velocidade está dentro do permitido' )
