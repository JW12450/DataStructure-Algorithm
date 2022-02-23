
def get_max(s):
    for j in range(1, n):
        if j == 1:
            s[0][j] += s[1][j - 1]
            s[1][j] += s[0][j - 1]
        else:
            s[0][j] += max(s[1][j - 1], s[1][j - 2])
            s[1][j] += max(s[0][j - 1], s[0][j - 2])
    return (max(s[0][n - 1], s[1][n - 1]))

"""
def get_max(s):
    dp = [[0]*n for i in range(2)]
    #print(s)
    dp[0][0] = s[0][0]
    dp[1][0] = s[1][0]
    if n == 1:
        return max((dp[0][n - 1], dp[1][n - 1]))
    dp[0][1] = s[1][0] + s[1][0]
    dp[1][1] = s[0][0] + s[1][1]
    #print(dp)
    for i in range(2,n):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + s[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + s[1][i]

    #print(dp)
    return max((dp[0][n-1], dp[1][n-1]))

"""

t = int(input())
for _ in range(t):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    print(get_max(sticker))