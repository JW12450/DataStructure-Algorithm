n = int(input())
card = list(map(int, input().split()))
card.insert(0,0)

dp = [0]*(n+1)
dp[1] = card[1]

for i in range(2, n+1):
    cand = []
    for j in range(1, i+1):
        cand.append(dp[i-j]+card[j])
    dp[i] = max(cand)
#dp[2] = max(dp[1]+card[1], card[2])
#dp[3] = max(dp[2]+card[1], dp[1]+card[2], dp[0]+card[3])
#dp[4] = max(dp[3]+card[1], dp[2]+card[2], dp[1]+card[3], dp[0]+card[4])

print(dp[n])