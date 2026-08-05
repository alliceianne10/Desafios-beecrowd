vence = { 'tesoura' : ['papel', 'lagarto'],
         'papel' : ['pedra', 'Spock'],
         'lagarto' : ['Spock', 'papel'],
         'Spock' : ['tesoura', 'pedra'],
         'pedra' : ['tesoura', 'lagarto']
}

N = int(input())

for i in range(1,N+1):
    S, R = input().split()

    if S == R:
        print(f'Caso #{i}: De novo!')
    elif S in vence[R]:
        print(f'Caso #{i}: Raj trapaceou!')
    else:
        print(f'Caso #{i}: Bazinga!')