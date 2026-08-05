N = int(input())

for i in range(N):
    entrada = list(input())

    a = int(entrada[0])
    b = entrada[1]
    c = int(entrada[2])

    if a == c:
        print(a*c)
    else:
        if b.isupper():
            print(c-a)
        else:
            print(a+c)