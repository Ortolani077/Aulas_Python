valorcasa=float(input('Qual o valor do imóvel? R$'))
salario=float(input('Qual o salário do comprador? R$'))
tempo=int(input('Em quantos anos vai ser pago?'))
prest= valorcasa / (tempo*12)

porc=salario/100*30

if prest>porc:
    print('Sua parcela será de R$ {:.2f}. Você não está apto para o financiamento'.format(prest))
else:
    print('Sua parcela será de R$ {:.2f}, Parabéns, você conseguiu o financiamento'.format(prest))