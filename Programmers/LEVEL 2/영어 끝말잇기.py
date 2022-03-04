def solution(n, words):
    check = []
    last = words[0][0]
    for i, w in enumerate(words):
        if w in check or last != w[0]:
                return [i % n + 1, (i//n)+1]
        else:
            check.append(w)
            last = w[-1]


    return [0,0]

from itertools import combinations

n, m = map(int, input().split())
n = [i for i in range(1,n+1)]
comb = list(combinations(n, m))
print(len(comb))
