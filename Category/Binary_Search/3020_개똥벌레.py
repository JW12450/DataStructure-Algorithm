import sys

n, h = map(int, sys.stdin.readline().split())

low = []
high = []
for _ in range(n//2):
    low.append(int(sys.stdin.readline()))
    high.append(int(sys.stdin.readline()))

low.sort()
high.sort()

#print(low)
#print(high)

#석순의 높이를 1부터 h까지 돌려보며 최소 값이 나올때마다 갱신, 같은 값이 나오면 누적
#석순의 높이를 선형 탐색하며 이분탐색을 통해 해당 높이일때 몇개의 석순을 부셔야하는지 계산
#이분탐색의 경우 임의의 값으로 시작하여 해당 높이와 같은 값이 나올때까지 mid가 해당 값보다 크면 앞쪽으로, mid가 해당 값보다 작으면 위쪽으로 줄여나가며 탐색
#이분탐색을 통해 해당 높이일 경우 몇개의 기둥을 부수며 통과해야하는지 알 수 있음

# 최종 누적해야 하는 값
cnt = 0
ans = n
for height in range(1, h+1):
    #바닥에서 자란 기둥부터 탐색
    min = 0
    start = 0
    end = n//2-1
    while start <= end:
        mid = (start+end)//2
        if low[mid] < height:
            start = mid+1
        else:
            end = mid-1

    #print('height',height)
    #print(n//2 -1  - end)
    min += (n//2 -1  - end)

    #위에서 자란 기둥탐색
    start = 0
    end = n // 2 - 1
    while start <= end:
        mid = (start + end) // 2
        if h+1-high[mid] > height:
            start = mid + 1
        else:
            end = mid - 1

    #print(n // 2 - 1 - end)
    min += (n // 2 - 1 - end)
    #print(min)
    #print()
    if min < ans:
        ans = min
        cnt = 1
    elif min == ans:
        cnt+=1

print(ans, cnt)