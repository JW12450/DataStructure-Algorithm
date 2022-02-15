import sys
#https://hongcoding.tistory.com/50
n,k = map(int, sys.stdin.readline().rstrip().split())

item = []
value = []
for _ in range(n):
    i, v = map(int, sys.stdin.readline().rstrip().split())
    item.append(i)
    value.append(v)

dp = [0 for i in range(n)]

if item[0] < k:
    dp[0] = value[0]

if item[0]+item[1] < k:
    dp[1] = dp[0]+value[1]
elif item[1] < k:
    dp[1] = max(dp[0], value[1])
else:
    dp[1] = dp[0]

for i in range(2, n):
    if item[i]