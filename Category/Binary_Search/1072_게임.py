import sys
"""
x, y = map(int, sys.stdin.readline().split())

if y/x * 100 > 10:
    rate = int(str(y/x * 100)[:2])
elif y/x * 100 > 0:
    rate = int(str(y/x * 100)[:1])
else:
    rate = 0
start = 1
end = 1000000000
print(rate)
if x == y or rate == 99:
    print(-1)
    sys.exit()
else:
    while start <= end:
        mid = (start + end)//2
        if (y+mid) / (x+mid) * 100 > 10:
            new = int(str((y+mid)/(x+mid) * 100)[:2])
        elif (y+mid) / (x+mid) * 100 > 0:
            new = int(str((y+mid)/(x+mid) * 100)[:1])
        else:
            rate = 0
        #print(new)
        if new == rate:
            start = mid + 1
        else:
            end = mid -1
            result = mid

print(result)
"""
x, y = map(int, sys.stdin.readline().split())

rate = y * 100 // x
start = 1
end = 1000000000

if x == y or rate == 99:
    print(-1)
    sys.exit()
else:
    while start <= end:
        mid = (start + end)//2
        new = (y+mid) * 100 // (x+mid)
        #print(new)
        if new == rate:
            start = mid + 1
        else:
            end = mid -1
            result = mid

print(result)

