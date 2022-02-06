import sys

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
cd_dict = {}