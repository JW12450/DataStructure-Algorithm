import sys

n, c = map(int, sys.stdin.readline().rstrip().split())

house = [int(sys.stdin.readline().rstrip()) for i in range(n)]
house.sort()


start = 1 #시작하는 거리의 최솟값
end = house[-1] - house[0]#시작하는 거리의 최댓값

# 임의의 거리값을 가장 첫번째 집의 좌표에 차례로 더해주며, 해당 임의의 거리값을 기준으로 공유기를 설치한다고 할때 설치되는 집의 수를 구함
# 이때 설치되는 공유기의 수가 주어진 조건보다 많으면, start를 mid+1로 올려서 더 넓은 거리값을 기준으로 공유기가 설치되도록
# 설치되는 공유기의 수가 주어진 조건보다 적으면, end의 값을 mid-1로 내려서 더 좁은 거리값을 기준으로 공유기가 설치되도록 한다
while start <= end:
    mid = (start + end)//2
    temp = house[0]
    cnt = 1

    for i in range(1, n):
        if house[i] >= temp + mid:
            cnt += 1
            temp = house[i]
    if cnt < c:
        end = mid -1
    else:
        start = mid + 1
        result = mid

print(result)