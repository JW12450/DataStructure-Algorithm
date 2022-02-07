import itertools
import sys
from itertools import product

n = int(sys.stdin.readline())
A=[]
B=[]
C=[]
D=[]
for _ in range(n):
    a, b, c, d = map(int, sys.stdin.readline().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

ab_dict = {}
ans = 0

for i in range(n):
    for j in range(n):
        ab = A[i] + B[j]
        if ab in ab_dict:
            ab_dict[ab] += 1
        else:
            ab_dict[ab] = 1

for i in range(n):
    for j in range(n):
        cd = -(C[i] + D[j])
        if cd in ab_dict:
            ans += ab_dict[cd]

print(ans)
#result = list(itertools.product(A, B, C, D))
