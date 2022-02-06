import sys

n, m = map(int, sys.stdin.readline().split())
tot = []
a1 = []
for _ in range(n):
    s = sys.stdin.readline().rstrip()
    a1.append(s)
    tot.append(s)
a2= []
for _ in range(m):
    a2.append(sys.stdin.readline().rstrip())

ans =[]
if len(a1)>len(a2):
    for a in a2:
        if a in a1:
            ans.append(a)
else:
    for a in a1:
        if a in a2:
            ans.append(a)

print(len(a2))
ans.sort()
for a in ans:
    print(a)