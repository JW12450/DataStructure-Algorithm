import sys

n = int(sys.stdin.readline())
array=[]
for _ in range(n):
    name, k, e, m = sys.stdin.readline().split()
    array.append([-int(k), int(e), -int(m), name])

array.sort()

for a in array:
    print(a[3])