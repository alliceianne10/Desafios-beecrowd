C = int(input())
T = input()

matriz = []

for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

soma = 0

for i in range(12):
    soma += matriz[i][C]

if T == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{soma/12:.1f}')