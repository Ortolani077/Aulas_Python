import math
ang = float(input('Digite o valor do ângulo: '))
ang1=math.radians(ang)
seno=math.sin(ang1)
cosceno=math.cos(ang1)
tangente=math.tan(ang1)

print('Usando o número', ang, 'temos o seno de ', seno, 'o cosceno de ', cosceno, 'e a tangente de ' , tangente )