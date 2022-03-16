
"""
import sys

n, m = map(int, sys.stdin.readline().split())
d = dict()
for _ in range(n):
    str = sys.stdin.readline().rstrip()
    d[str] = 1
cnt = 0
for _ in range(m):
    str = sys.stdin.readline().rstrip()

    if str in d:
        cnt += 1

print(cnt)


"""
from string import ascii_lowercase
al = list(ascii_lowercase)
print(al)