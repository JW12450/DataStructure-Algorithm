import sys

n = int(sys.stdin.readline())

array = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    array.append([y,x])

array.sort()

for i in range(n):
    print(array[i][1], end=" ")
    print(array[i][0])