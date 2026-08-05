N = int(input())
for _ in range(N):
    a = input()

    novo_a = ''
    for _ in a:
     novo_a += chr(ord(_) +3 ) if _.isalpha() else _
    a = novo_a[::-1]

    a = a[:len(a)//2] + ''.join([chr(ord(_)-1) for _ in a[len(a)//2:]]) 
    print(a)
