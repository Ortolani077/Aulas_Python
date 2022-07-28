import random
alun1=input('Nome do aluno1')
alun2=input('Nome do aluno2')
alun3=input('Nome do aluno3')
alun4=input('Nome d aluno4')
lis=(alun1, alun2, alun3, alun4)
s=random.sample(lis,4)

print('A ordem para ser apresentada é a seguinte:', s)