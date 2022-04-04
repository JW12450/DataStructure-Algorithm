while True:
    d = list(map(int, input().split()))
    if d[0] == 0 and d[1]==0 and d[2]== 0:
        break
    c = max(d)
    d.remove(c)
    a = d[0]
    b = d[1]
    if a*a + b*b == c*c:
        print("right")
    else:
        print("wrong")