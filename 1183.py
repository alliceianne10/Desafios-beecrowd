O = input()
matriz = []

for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)

soma = 0
for i in range(12):
    for j in range(1+i,12):
        soma += matriz[i][j]

if O == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{soma/66:.1f}')