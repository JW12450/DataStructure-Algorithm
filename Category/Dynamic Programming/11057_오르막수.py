n = int(input())

dp = [[0 for i in range(10)]for j in range(n+1)]
for i in range(10):
    dp[1][i] = 10-i
#print(dp)

for i in range(2,n+1):
    for j in range(0,10):
        for k in range(j,10):
            dp[i][j] += dp[i-1][k]
print(dp[n][0] % 10007)

#for i in range(2, n):
#    dp[i] =