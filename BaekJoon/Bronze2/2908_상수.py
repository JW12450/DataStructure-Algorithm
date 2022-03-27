a, b = map(int, input().split())

a = list(str(a))
a.reverse()
a = int("".join(a))

b = list(str(b))
b.reverse()
b = int("".join(b))

print(max(a,b))