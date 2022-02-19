import math
n = int(input())

dp = [[[]for j in range(10)]for i in range(n+1)]

for i in range(10):
    dp[1][i] = 1

for i in range(2, n+1):
    dp[i][0] = dp[i-1][1]
    for j in range(1,9):
        #print(f'dp[{i}]][{j}] = dp[{i-1}][{j-1}] + dp[{i-1}][{j+1}] : {dp[i-1][j-1] + dp[i-1][j+1]}')
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    dp[i][9] = dp[i-1][8]

#for d in dp:
#    print(d)

cnt = 0
for i in range(1,10):
    cnt += dp[n][i]
print(cnt % 1000000000)