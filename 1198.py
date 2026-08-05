while True:
    try:
        has, opo = map(int, input().split())

        print(abs(opo - has))

    except EOFError:
        break