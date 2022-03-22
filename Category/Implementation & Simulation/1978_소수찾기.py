def check(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False

    return True

import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

count = 0
for i in range(n):
    if check(array[i]):
        count+=1

print(count)