import sys
from collections import Counter

n = int(sys.stdin.readline())

array = []
for i in range(n):
    array.append(int(sys.stdin.readline()))

array.sort()
print(round(sum(array)/n))
print(array[n//2])

cnt = Counter(array)
order = cnt.most_common(2)

#print(order)

ans = 0
#print(order[0][1])
if len(order) > 1:
    if (order[0][1] == order[1][1]):
        ans = 1
else:
    ans = 0
print(order[ans][0])

print(array[-1] - array[0])