n = int(input())

weight = [0 for i in range(n)]
for i in range(n):
    weight[i] = int(input())

weight.sort()
for i in range(1,n+1):
    weight[i-1] = weight[i-1]*(n+1-i)

print(max(weight))