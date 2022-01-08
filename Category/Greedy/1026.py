n = int(input())

a = []
b = []

a = list(map(int, input().split()))
b = list(map(int, input().split()))

sorted_a = a.sort()

sum = 0
for i in range(n):
    sum += a[i] * max(b)
    b.remove(max(b))

print(sum)