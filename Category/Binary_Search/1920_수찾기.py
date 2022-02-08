import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
check = {}
for i in range(n):
    check[array[i]] = 1

m = int(sys.stdin.readline())
array2 = list(map(int, sys.stdin.readline().split()))

#print(check)
for num in array2:
    if num in check:
        print(1)
    else:
        print(0)