while True:
    N = int(input())
    if N == 0 :break 

    numeros = list(map(int, input().split()))
    print(f'Mary won {numeros.count(0)} times and John won {numeros.count(1)} times')
    