import math
catoposto= float(input('Digite o comprimento do cateto oposto:'))
catadjascente=float(input('Digite o comprimento do cateto adjascente:'))
hip=math.hypot(catoposto, catadjascente)
print(f'A hipotenusa é:', hip)