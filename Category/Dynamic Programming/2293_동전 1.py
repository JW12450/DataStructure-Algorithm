n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
#print(coins)

dp = [0 for i in range(k+1)]

dp[0] = 1

for i in coins:
    for j in range(1,k+1):
        if j-i >=0:
            dp[j] += dp[j-i]

print(dp)
"""
1111111111
111111112
11111122
1111222
112222
22222
511111
52111
5221
55

"""






