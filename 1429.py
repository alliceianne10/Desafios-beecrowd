import math
while True:
    N = input()

    if N == '0':
        break 

    dig = len(N)

    soma = 0
    for i in range(dig):
        soma += int(N[i]) * math.factorial(dig-i)

    print(soma)