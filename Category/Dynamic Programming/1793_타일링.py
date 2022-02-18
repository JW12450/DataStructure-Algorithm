#An = An-2 * 3
def tile(n):
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 3

    for i in range(3, n+1):
        dp[i] = dp[i-2]*2 + dp[i-1]

    print(dp[n])

dp = [0] * (251)
dp[0] = 1
dp[1] = 1
dp[2] = 3
while True:
    try:
        n = int(input())
        for i in range(3, n + 1):
            dp[i] = dp[i - 2] * 2 + dp[i - 1]

        print(dp[n])
    except:
        break