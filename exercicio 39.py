idade=int(input('Digite o ano de seu nascimento'))
idade2= 2022-idade
idade3=idade2-18
idade4=18-idade2
idade5=idade2-18

if idade2<18:
    print('Você ainda não tem idade para se alistar no serviço militar, ainda faltam {} anos'.format(idade4))
elif idade2==18:
    print('Já está na hora de se alistar no serviço militar')
elif idade2>18:
    print('Já se passaram {} anos,se ainda não se alistou, procure\na'
          ' junta militar da sua cidade e se aliste !!'.format(idade5))
