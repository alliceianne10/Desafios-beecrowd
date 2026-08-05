a = int(input())
b = int(input())

inicio = min(a, b) + 1
fim = max(a, b)

soma = 0

for i in range(inicio, fim):
    if i % 2 != 0:
        soma += i

print(soma)