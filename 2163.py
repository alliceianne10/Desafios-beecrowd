N,M = map(int, input().split())

matriz = []

for i in range(N):
       linha = list(map(int,input().split()))
       matriz.append(linha)

achou = False

for i in range(1, N-1):
    for j in range(1, M-1):
        if matriz[i][j] == 42:
           if(
             matriz[i-1][j-1]==7 and 
             matriz[i][j-1] == 7 and 
             matriz[i+1][j-1]==7 and 
             matriz[i+1][j] == 7 and 
             matriz[i+1][j+1]==7 and 
             matriz[i][j+1]==7 and 
             matriz[i-1][j+1]==7 and 
             matriz[i-1][j]==7
        ):
            print(f'{i+1} {j+1}')
            achou = True
            break 
        if achou:
           break

if not achou:
   print('0 0')