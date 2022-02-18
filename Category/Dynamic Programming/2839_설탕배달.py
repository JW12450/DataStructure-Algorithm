import sys

n = int(sys.stdin.readline())

#dp 테이블
d = [9999]*(n*5)
d[3] = 1
d[5] = 1

#bottom-up 방식
for i in range(6, n+1):
    d[i] = min(d[i-3], d[i-5])+1

if d[n] < 9999:
    print(d[n])
else :
    print(-1)