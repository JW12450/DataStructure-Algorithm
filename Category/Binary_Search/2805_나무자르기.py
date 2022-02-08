import sys

n, m = map(int, sys.stdin.readline().split())

array = list(map(int, sys.stdin.readline().rstrip().split()))
right = max(array)
left = 0

while True:
    height = (right+left) //2
    sum = 0
    cnt = 0
    for a in array:
        dif = a - height
        if dif > 0:
            sum += dif
            cnt += 1

    if sum < m:
        right = height
    elif sum >= m + cnt:
        left = height
    else:
        print(height)
        break
    """
    print(height)
    print(sum)
    print(left, right)
    print()
    """



"""
h = max(array)
cut = [i-h for i in array]
s = sum(cut)

cnt = 0
while True:
    tree = 0
    for a in cut:
        if a>0:
            tree += a
        else:
            continue

    if tree < m:
        for i in range(n):
            cut[i] += 1
        cnt += 1
    else:
        break
    #print(cut)

print(h - cnt)
"""
