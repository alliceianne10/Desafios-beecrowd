L = int(input())
T = input()

soma = 0

for i in range(12):
    for j in range(12):
        n = float(input())
        if i == L:
            soma += n

if T.upper() == "S":
    print(soma)
else:
    media = soma / 12
    print(media)