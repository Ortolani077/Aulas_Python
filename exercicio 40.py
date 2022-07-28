nota1=float(input('Digite a primeira nota: '))
nota2=float(input('Digite a segunda nota: '))
cal=nota1+nota2
med= cal/2
if med<5.0:
    print('Sua média foi de {}, você está \033[31mREPROVADO'.format(med))
elif med<7 and med>=5:
    print('Sua média foi de {}, você está em\033[34m Recuperação'.format(med))
else:
    print('Parabéns, sua nota foi {}, você está\033[32m Aprovado'.format(med))

