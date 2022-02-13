import sys

n = int(sys.stdin.readline())

tree = []
dp = []
for i in range(n):
    dp.append([0 for j in range(i+2)])

for i in range(n):
    tree.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(i+1):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + tree[i][j]


print(max(dp[n-1]))
