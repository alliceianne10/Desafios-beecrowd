N = int(input())

for i in range(1,N+1):
    n,k = map(int, input().split())

    pos = 0
    for j in range(2,n+1):
        pos = (pos + k) % j

    print(f'Case {i}: {pos +1}')
