n = int(input())
a = list(map(int, input().split()))

dp = [0 for i in range(n)]
result = -1001
for i in range(n):
    dp[i] = max(dp[i-1]+a[i], a[i])
    result = max(result, dp[i])
    #print(result)

#print(dp)
print(result)