N = int(input())

for i in range(N):
    x, y = map(int, input().split())

    if x % 2 == 0:
        numero = x+1
    else:
        numero = x
    soma = 0 

    for j in range(y):
        soma += numero
        numero += 2
    print(soma)
