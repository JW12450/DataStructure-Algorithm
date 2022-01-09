a, b = map(int, input().split())

Cnt = 1
while True:
    if (b == a):
        print(Cnt)
        break
    if (b <= 0):
        print(-1)
        break
    if (b%2 == 0):
        b = b/2
        Cnt += 1
    else:
        b -= 1
        b = b/10
        Cnt += 1