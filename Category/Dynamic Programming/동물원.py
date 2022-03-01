"""
dp = [[0for j in range(4)] for i in range(100001)]
dp[1][0] = 1
dp[1][1] = 1
dp[1][2] = 1
dp[1][3] = 1

for i in range(2, n+1):
    dp[i][0] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3]
    dp[i][1] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]
    dp[i][2] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]
    dp[i][3] = dp[i - 1][0]

print(sum(dp[n]))

dp = [[0for j in range(3)] for i in range(n+1)]
dp[1][0] = 1
dp[1][1] = 1
dp[1][2] = 1

for i in range(2, n+1):
    dp[i][0] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]
    dp[i][1] = dp[i - 1][0] + dp[i - 1][2]
    dp[i][2] = dp[i - 1][0] + dp[i - 1][1]

print(sum(dp[n]))
"""
n = int(input())

dp = [0 for j in range(3)]
dp[0] = 1
dp[1] = 1
dp[2] = 1

for i in range(2, n+1):
    a, b, c = dp[0], dp[1], dp[2]
    dp[0] = a + b + c
    dp[1] = a + c
    dp[2] = a + b

print(sum(dp) % 9901)