par = []
impar = []

for i in range(15):
    N = int(input())
    
    if N % 2 == 0:
        par.append(N)
        if len(par) == 5:
            for j, v in enumerate(par):
                print(f'par[{j}] = {v}')
            par = []
    else:
        impar.append(N)
        if len(impar) == 5:
            for j,v  in enumerate(impar):
                print(f'impar[{j}] = {v}')
            impar = []

#Colocando os elementos quando a lista tem menos de 5 elementos

for j,v in enumerate(impar):
    print(f'impar[{j}] = {v}')

for j,v in enumerate(par):
    print(f'par[{j}] = {v}')