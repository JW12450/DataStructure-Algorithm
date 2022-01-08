a, b, c = map(int, input().split())

point = 0
while True:
    if (a + point*b < point*c):
        print(point)
        break
    point += 1