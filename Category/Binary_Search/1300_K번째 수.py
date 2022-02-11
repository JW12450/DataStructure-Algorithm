import sys

n = int(input())
k = int(input())

"""
이중배열을 사용하면 메모리 초과
a = [[[]for i in range(n)]for j in range(n)]
for i in range(1,n+1):
    for j in range(1,n+1):
        a[i-1][j-1] = i*j

for j in range(len(a)):
    print(a[j])
"""


start = 1
end = n*n
#각 행별로 접근한다고 생각할때 해당 행에서 우리가 얻을 수 있는 정보는 min(임의의 수//해당 행의 번호, n)만큼이 임의의수보다 작은 수의 개수
while start <= end:
    mid = (start+end)//2

    cnt = 0
    for i in range(1, n+1):
        cnt += min(mid//i, n)

    if cnt >= k:
        end = mid-1
    else:
        start = mid+1

print(start)