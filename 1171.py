N = int(input())

numeros = []

for i in range(N):
    entrada = int(input())
    numeros.append(entrada)
    
n_n_repetidos = list(set(numeros))
n_n_repetidos = sorted(n_n_repetidos)


for i in range(len(n_n_repetidos)):
    cont = numeros.count(n_n_repetidos[i])
    print(f'{n_n_repetidos[i]} aparece {cont} vez(es)')