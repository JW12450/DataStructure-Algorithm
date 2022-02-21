import sys
n = int(sys.stdin.readline())
t = []
p = []
dp = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    t.append(a)
    p.append(b)
    dp.append(b)

dp.append(0)

for i in range(n-1, -1, -1):
    if t[i]+i > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], p[i]+ dp[i+t[i]])

print(dp[0])
#뒤에서부터 접근해보자
"""
dp[i+1] : 다음날에 일했을때 얻을 수있는 값
pay[i] + dp[i+day[i]] :그날 일을 하고 일이 끝나는 다음날에 일한다 가정했을때의 값
이 둘을 비교하여 큰값을 넣어줌.
"""



"""
#1일차부터 n일차까지 해당 날짜까지 받을 수 있는 최대 수당 저장
for i in range(1,n+1):
    if t[i] == 1:
        dp[i] = dp[i-1] + p[i]
    else:
        #오늘날짜부터 하는 일이 끝난 날의 최댓값 = 전날값'
        dp[i + t[i]-1] = max(dp[i + t[i]-2],p[i])+dp[i-1]
        #print(i,'일차: ',dp[1:], dp[i])
ans = 0
for i in range(n+1):
    ans = max(ans, dp[i])

print(ans)
"""

