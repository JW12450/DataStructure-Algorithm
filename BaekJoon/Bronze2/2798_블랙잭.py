from itertools import combinations
n, m = map(int, input().split())
l = list(map(int, input().split()))
comb = list(combinations(l, 3))

ans = 0
for c in comb:
    s = sum(c)
    if s > m:
        continue
    if s > ans:
        ans = s

print(ans)