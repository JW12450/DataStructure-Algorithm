import sys

n, m = map(int, sys.stdin.readline().split())

a1 = set()
for i in range(n):
    s = sys.stdin.readline().rstrip()
    a1.add(s)

a2= set()
for _ in range(m):
    s = sys.stdin.readline().rstrip()
    a2.add(s)

ans = list(a1.intersection(a2))
print(len(ans))

if len(ans) != 0:
    ans.sort()
    for a in ans:
        print(a)