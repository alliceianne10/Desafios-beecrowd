n = int(input())

for i in range(n): 
    a = int(input())
    soma = 0
    for t in range(1,a):
        if(a%t==0):
            soma=soma+t
    if (soma>2):
        print(f'{a} nao eh primo')
    else:
        print(f'{a} eh primo')
    