
N = int(input())

if N % 2 == 0:
    a = N*N/2
    print(f'{a:.0f} casas brancas e {a:.0f} casas pretas')
else:
    a = N*N /2 + 0.5
    b = N*N/2 - 0.5
    print(f'{a:.0f} casas brancas e {b:.0f} casas pretas')