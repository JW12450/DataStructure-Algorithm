from itertools import combinations, permutations

n, m = map(int, input().split())

array = [i for i in range(1, n+1)] * m
#array = array*m

#print(array)
comb = list(set(combinations(array, m)))

#comb = list(set(comb))
comb.sort()
for c in comb:
    #print(list(c), sorted(c))
    if list(c) == sorted(c):
        print(" ".join(map(str, c)))
