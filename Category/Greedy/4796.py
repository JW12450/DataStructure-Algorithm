i = 1
while True:
    l, p, v = map(int, input().split())

    if (p == 0 and l == 0 and v == 0):
        break

    Cnt = 0
    Cnt += (v // p)*l

    if (v%p <= l):
        Cnt += v%p
    else:
        Cnt += l

    print(f'Case {i}: {Cnt}')
    i += 1