x = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP테이블 초기화
d = [0]*100000

for i in range(2, x + 1):
    #현재의 수에서 1을 빼는 경우
    d[i] = d[i-1]+1

    if i%2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)


print(d[x])


"""
import sys

n = int(sys.stdin.readline())

dp = [0] * (n+1)

for i in range(2, n+1):
    dp[i] = dp[i-1]+1
    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[n])
"""