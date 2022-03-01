import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for i in range(n)]

l = [i for i in range(n)]
comb = list(combinations(l, n//2))

min = 99999
for c in comb:
    a = c
    b = []
    for i in range(n):
        if i not in a:
            b.append(i)
    pair_a = list(combinations(a, 2))
    pair_b = list(combinations(b, 2))

    sum_a = 0
    sum_b = 0
    #print(pair_a, pair_b)
    for p in pair_a:
        sum_a += graph[p[0]][p[1]]
        sum_a += graph[p[1]][p[0]]
    for p in pair_b:
        sum_b += graph[p[0]][p[1]]
        sum_b += graph[p[1]][p[0]]
    #print(sum_a, sum_b)

    if abs(sum_a - sum_b) < min:
        min = abs(sum_a - sum_b)

print(min)
