import sys

n = int(sys.stdin.readline())
if n == 1:
    print(int(input()))
    sys.exit()
if n == 2:
    print(int(input()) + int(input()) )
    sys.exit()
stairs = [0]
for _ in range(n):
    stairs.append(int(sys.stdin.readline()))

dp = [0]*(301)
dp[1] = stairs[1]
dp[2] = stairs[1]+stairs[2]
dp[3] = max(stairs[1]+stairs[3], stairs[2]+stairs[3])

for i in range(4, n+1):
    dp[i] = max(dp[i-3]+ stairs[i-1]+stairs[i], dp[i-2]+stairs[i])

#print(dp)
print(dp[n])