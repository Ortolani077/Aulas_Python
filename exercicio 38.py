valor1=int(input('Digite um número inteiro'))
valor2=int(input('Digite outro número inteiro'))

if valor1>valor2:
    print('O primeiro valor ({}) é maior que o segundo valor ({}) '.format(valor1, valor2))
elif valor1==valor2:
    print( 'Não existe valor maior, os dois valores são iguais')
elif valor1<valor2:
    print( ' O segundo valor ({}) é maior que o primeiro valor ({}) '.format(valor2,valor1))