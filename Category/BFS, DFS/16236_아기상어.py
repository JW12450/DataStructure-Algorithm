import sys
from collections import deque

n = int(sys.stdin.readline())

graph = [list(map(int, sys.stdin.readline().rstrip().split()))for _ in range(n)]
cur_x, cur_y = 0, 0
size = 2
#현재위치 탐색
for x in range(n):
    for y in range(n):
        if graph[x][y] == 9:
            cur_x, cur_y = x, y
graph[cur_x][cur_y] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
#두 좌표 지점간의 거리
def dist(a,b):
    count = [[0 for i in range(n)] for j in range(n)]
    visited = [[False for i in range(n)] for j in range(n)]
    queue = deque()
    queue.append((a[0], a[1]))
    visited[a[0]][a[1]] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and graph[nx][ny] <= size:
                queue.append((nx, ny))
                visited[nx][ny] = True
                count[nx][ny] = count[x][y] + 1

    if visited[b[0]][b[1]]:
        return count[b[0]][b[1]]
    else:
        return 99999

#현재 그래프 상에서 먹을 수 있는 물고기를 탐색하는 함수
#크기를 확인한 후, 해당 물고기까지의 거리도 구하고, 최단 거리가 나오면 후보 리스트를 리셋, 최단거리와 같은 거리가 나오면 후보리스트에 추가
def find_can_eat_cand(cur_x, cur_y):
    cand = []
    min = 99999
    for x in range(n):
        for y in range(n):
            if graph[x][y] >= size or graph[x][y] == 0:
                continue
            elif dist([cur_x,cur_y], [x,y]) == 99999:
                continue
            elif dist([cur_x,cur_y], [x,y]) < min:
                min = dist([cur_x,cur_y], [x,y] )
                #최단 거리를 찾은 경우 기존의 cand 리스트 초기화후 추가
                cand = []
                cand.append( (x,y) )
            #최단거리와 같은 경우 해당 좌표도 추가
            elif dist([cur_x,cur_y], [x,y]) == min:
                cand.append( (x,y) )
    return cand, min

time = 0
cnt = 0
while True:
    cand, min = find_can_eat_cand(cur_x, cur_y)
    """
        for g in graph:
        print(g)
    print("cur: ", cur_x, cur_y)
    print("size: ", size)
    print("time: ", time)
    print("cand: ", cand)
    print()
    """
    #더 이상 먹을 물고기가 없는 경우
    if len(cand) == 0:
        break
    #먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
    if len(cand) == 1:
        cur_x, cur_y = cand[0][0], cand[0][1]
        graph[cur_x][cur_y] = 0
        time += min
        cnt += 1
    #먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다
    if len(cand) > 1:
        cur_x, cur_y = cand[0][0], cand[0][1]
        graph[cur_x][cur_y] = 0
        time += min
        cnt += 1

    if cnt == size:
        size += 1
        cnt = 0
print(time)

"""
[4, 3, 2, 1]
[0, 0, 0, 0]
[0, 0, 0, 0]
[1, 2, 3, 4]
cur:  2 2
size:  2
time:  0
cand:  [(0, 3), (3, 0)]

[4, 3, 2, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
[1, 2, 3, 4]
cur:  0 3
size:  2
time:  3
cand:  [(3, 0)]

[4, 3, 2, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 2, 3, 4]
cur:  3 0
size:  3
time:  9
cand:  [(3, 1)]

[4, 3, 2, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 3, 4]
cur:  3 1
size:  3
time:  10
cand:  [(0, 2)]

[4, 3, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 3, 4]
cur:  0 2
size:  3
time:  14
cand:  []

14

"""