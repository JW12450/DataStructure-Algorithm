import sys

n = int(sys.stdin.readline())
city =  list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline())

start = 1
end = max(city)

while start <= end:
    mid = (start+end)//2

    cnt = 0
    for c in city:
        if mid <= c:
            cnt += mid
        else:
            cnt += c
    # 예산 배정액의 합이 k를 넘는 경우, 이진탐색의 범위를 내림
    if cnt > m:
        end = mid-1
    else:
        start = mid + 1
        result = mid

print(result)