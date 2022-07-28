n1= float(input('Digite um número: '))
n2=float(input('Digite outro número: '))
n3=float(input('Digite mais um número: '))
list=[n1,n2,n3]
if n1>n2>n3:
    print(f'o numero maior é', n1, 'é o menor é:', n3)
if n1>n3>n2:
    print(f'O maior número é o: ' , n1, 'e o menor é o:', n2)
if n2>n1>n3:
    print(f'O maior número é o:', n2, 'e o menor o:',n3)
if n2>n3>n1:
    print(f'O número maior é o: ', n2, 'e o menor:', n1 )
if n3>n2>n1:
    print(f'O maior número é o: ', n3, ' e o menor:' , n1)
if n3>n1>n2:
    print(f' O maior número é o:' , n3 , 'e o menor é o ', n2)
else:
    print('==fim==')





