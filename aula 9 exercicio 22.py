nome=input('Digite seu nome:')
print(f'Seu nome em maíusculas:', nome.upper())
print(f'Seu nome em minúsculas:', nome.lower())
dividido= nome.split()
primeiro=len(dividido[0])

nome2 =''.join(dividido)
nomeint=len(nome2)


print(f'Seu nome tem', nomeint, 'caracteres ao todo sem contar os espaços, e seu primeiro nome tem', primeiro, 'caracteres')



