import random
nom=input('Escreva o nome do aluno1:')
nom2=input('Escreva o nome do aluno2:')
nom3=input('Escreva o nome do aluno3')
nom4=input('Escreva o nome do aluno4')

r=random.choice([nom,nom2,nom3,nom4])

print('O aluno sorteado é:', r)