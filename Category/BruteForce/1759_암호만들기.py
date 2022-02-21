from itertools import combinations
l, c = map(int, input().split())
password = list(input().split())

password.sort()
comb = list(combinations(password, l))
vowel = ['a','e','i','u','o']
for c in comb:
    a_count = 0
    b_count = 0
    for a in c:
        if a in vowel:
            a_count += 1
        else:
            b_count += 1
    if a_count >= 1 and b_count >= 2:
        print("".join(c))



