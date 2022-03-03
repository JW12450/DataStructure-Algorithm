n, k = map(int, input().split())

#0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수
"""
n = 20
k = 4 일때,

0부터 20까지의 정수 2개를 더해서 그 합이 20이 되는 경우의 수
0 20
1 19
2 18
...
19 1
20 0

"""
dp = [[0]*201 for i in range(201)]
for i in range(201):
    dp[1][i] = 1
    dp[2][i] = i+1

for i in range(2,201):
    dp[i][1] = i
    for j in range(2,201):
        dp[i][j] = (dp[i][j-1] +dp[i-1][j]) % 1000000000

print(dp[k][n])



