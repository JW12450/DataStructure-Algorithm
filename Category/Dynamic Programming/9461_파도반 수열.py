import sys

t = int(sys.stdin.readline())

def getP(n):
    dp = [0]*101
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = dp[1]+dp[3] #2
    dp[5] = dp[4]       #2

    for i in range(6,n+1):
        dp[i] = dp[i-5]+dp[i-1]
    """
    dp[6] = dp[1]+dp[5] #3
    dp[7] = dp[2]+dp[6] #4
    dp[8] = dp[3]+dp[7] #5
    dp[9] = dp[4]+dp[8]
    """

    return dp[n]

for _ in range(t):
    n = int(sys.stdin.readline())
    print(getP(n))