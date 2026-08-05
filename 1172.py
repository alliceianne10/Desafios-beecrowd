vetor = []
for j in range(10):
    entrada = int(input())
    vetor.append(entrada)

for i in range(10):
    if vetor[i] <= 0:
        vetor[i] = 1

for k in range(10):
    print(f'X[{k}] = {vetor[k]}')
