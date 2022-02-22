import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

house = []
bbq = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append([i,j])
        elif graph[i][j] == 2:
            bbq.append([i,j])

def dist(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

comb = list(combinations(bbq, m))
#print(comb)
#각각의 집에서 폐업시키지 않고 살아남은 치킨집들의 거리중 최솟값만을 저장

dist_list = []
for c in comb:
    # c 즉, 한 조합 안에 있는 치킨집들로부터 모든 집들의 거리를 구하고, 이때의 최솟값만을 해당 집에서 치킨집까지의 거리로 추가
    distance = 0  # 한 집당 각각의 조합 별 도시의 치킨 거리의 합
    for h in house: #치킨집 하나와 모든 집들간의 거리
        this_h = []
        for cc in c:
            this_h.append(dist(h,cc))
        distance += min(this_h) #해당 집에서 가장 가까운 치킨집까지의 거리
    dist_list.append(distance)
print(min(dist_list))


