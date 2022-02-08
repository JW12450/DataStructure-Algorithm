import sys, bisect

k, n = map(int, sys.stdin.readline().split())

array = [int(sys.stdin.readline().rstrip()) for _ in range(k)]

start = 1
end = max(array)

while start <= end:
    mid = (start + end)//2
    lines = 0
    for a in array:
        lines += a//mid

    # 선의 개수가 모자르므로, 더 작은 단위로 나눠서 값을 늘려야 함
    if lines < n:
        end = mid-1
    elif lines >= n:
        start = mid+1

    #print(start,end)

print(end)
