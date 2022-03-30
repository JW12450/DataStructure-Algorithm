from string import ascii_lowercase

a = input()
alp = list(ascii_lowercase)
ans = [-1 for i in range(len(alp))]
for i in range(len(a)):
    if ans[alp.index(a[i])] == -1:
        ans[alp.index(a[i])] = i

str = " ".join(map(str, ans))
print(str)