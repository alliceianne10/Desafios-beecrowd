n = int(input())
vetor = [n]

for i in range(9):
    vetor.append(vetor[i] *2)

for j in range(10):
    print(f'N[{j}] = {vetor[j]}')

