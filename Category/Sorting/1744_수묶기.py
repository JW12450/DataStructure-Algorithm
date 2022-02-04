"""
import sys, heapq

n = int(sys.stdin.readline())

heap = []
for _ in range(n):
    i = int(sys.stdin.readline())
    heapq.heappush(heap, (-i, i))

sum = 0

while len(heap) > 0:
    if len(heap) == 1:
        sum += heapq.heappop(heap)[1]
        break
    #print(heapq.heappop(heap))
    i = heapq.heappop(heap)[1]
    j = heapq.heappop(heap)[1]
    print(i,j)
    sum += i*j

print(sum)
"""
import sys

n = int(sys.stdin.readline())
array = []
for _ in range(n):
    array.append(int(sys.stdin.readline()))

if len(array) == 1:
    print(array.pop())
    sys.exit()

plus = []
minus = []
zero = []
one = []
for a in array:
    if a>1:
        plus.append(a)
    elif a == 1:
        one.append(a)
    elif a < 0:
        minus.append(a)
    else:
        zero.append(0)

plus.sort()
minus.sort(reverse=True)

sum = 0
while True:
    if len(minus) == 0:
        break
    elif len(minus) == 1:
        if len(zero)> 0:
            break
        else:
            sum += minus.pop()
    else:
        i = minus.pop()
        j = minus.pop()
        sum += i*j

while True:
    if len(plus) == 0:
        break
    elif len(plus) == 1:
        sum += plus.pop()
    else:
        i = plus.pop()
        j = plus.pop()
        sum += i * j

sum += len(one)
print(sum)

"""
while len(array) > 0:
    if len(array) == 1:
        sum += array.pop()
        break
    i = array.pop()
    j = array.pop()

    if i > 0 and j > 0:
        if i == 1 or j == 1:
            sum += i + j
        else:
            sum += i*j
    elif i > 0 and j == 0:
        if len(array) >= 1:
            k = array.pop(0)
            sum += i
            sum += 0
        else:
            sum += i
    elif i == 0 and j == 0:
        if len(array) > 2:
            array.pop(0)
            array.pop(0)
        if len(array) == 1:
            array.pop(0)
        else:
            break
    elif i == 0 and j < 0:
        if len(array) >= 1:
            k = array.pop(0)
            sum += j
            sum += 0
    elif i > 0 and j < 0:
        sum += i + j
    else:
        array.append(j)
        array.append(i)
        i = array.pop(0)
        j = array.pop(0)
        sum += i*j
    print(array, sum)
print(sum)

while len(array) != 0:
    if len(array) == 1:
        sum += array.pop()
        break
    i = array.pop()
    j = array.pop()
    if i == 0 and len(array) > 1:
        k = array.pop(0)
        sum += i*k
        array.append(j)
        #print(array, sum)
        continue
    if j == 0 and len(array) > 1:
        k = array.pop(0)
        sum += j*k
        array.append(j)
        #rint(array, sum)
        continue
    if i*j > 0:
        if j == 1:
            sum += i + j
        else:
            sum += i*j
    elif i*j == 0:
        if len(array) >= 1:
            k = array.pop()

            if j*k == 0:
                sum += i + j*k
        else:
            sum += max(i,j)
    else:
        sum += i + j
    #print(array, sum)
print(sum)
"""