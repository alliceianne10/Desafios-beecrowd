while True:
    N = int(input())

    if N == 0:break 

    matriz = []

    for i in range(N):
        linha = []
        for j in range(N):
            valor = min(i,j,N-1-j,N-1-i) + 1
            linha.append(valor)
        matriz.append(linha)
    
    for i in range(N):
        linha_formatada = ''
        for j in range(N):
            linha_formatada += f'{matriz[i][j]:3d}'

            if j <N-1:
               linha_formatada += ' '
        print(linha_formatada)

    print()