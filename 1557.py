while True:
    N = int(input())

    if N == 0:
        break 

    T = len(str(2**((N-1)*2)))
    

    matriz = []

    for i in range(N):
        linha = []
        for j in range(N):
            valor = 2**(i+j)
            linha.append(valor)
        matriz.append(linha)
    
    for i in range(N):
        linha_formatada = ''
        for j in range(N):
            linha_formatada += f'{matriz[i][j]:{T}d}'
        
            if j< N-1:
                linha_formatada +=' '
        print(linha_formatada)
    print()

    
