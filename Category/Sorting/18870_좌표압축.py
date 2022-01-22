"""
import sys
from collections import Counter

n = int(sys.stdin.readline())

array = list(map(int, sys.stdin.readline().split()))

cnt = Counter(array)
order = cnt.most_common()

order.sort()

#print(array)
#print(cnt)
#print(order)

#print(order.index((array[0],array.count(array[0]))))
for i in range(n):
    print(order.index((array[i],array.count(array[i]))), end=" ")

시간초과
"""
import sys
from collections import Counter
n = int(sys.stdin.readline())

if n == 1:
    print(0)
else:
    array = list(map(int, sys.stdin.readline().split()))
    cnt = Counter(array)
    order = cnt.most_common()

    sorted_array = sorted(array)

    # 값과 압축된 값이 포함된 딕셔너리
    result = {}
    count = cnt[sorted_array[1]]

    num = 0
    for i in range(n):
        if sorted_array[i] not in result.keys():
            result[sorted_array[i]] = num
            num += 1

    for i in range(n):
        print(result[array[i]], end=" ")
