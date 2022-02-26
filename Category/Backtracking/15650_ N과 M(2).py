from itertools import combinations

n, m = map(int, input().split())

array = [i for i in range(1, n+1)]
comb = list(combinations(array, m))

for c in comb:
    for a in c:
        print(a, end = " ")
    print()


"""
분할 정복 이용 풀이법
"""
s = []
def dfs(start):
    if len(s) == m:
        print(' '.join(map(str,s)))
        return 

    for i in range(start, n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()

dfs(1)