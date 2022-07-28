import random
numero=random.randint(0,5)
escolha=int(input('Escolha um número de 0 á 5:'))
if escolha==numero:
    print(f'Acertou, mizeravi')
else:
    print(f' Errrou')