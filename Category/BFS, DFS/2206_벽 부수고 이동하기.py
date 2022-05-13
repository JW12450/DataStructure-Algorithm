"""
import sys, copy
#from itertools import combinations
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph_ = [ list(map(int, sys.stdin.readline().rstrip())) for i in range(n)]

if n == 1 and m == 1:
    print(1)
    sys.exit()

wall_list = []
for i in range(n):
    for j in range(m):
        if graph_[i][j] == 1:
            wall_list.append( (i, j) )

route = m*n - len(wall_list)
#경로에 도착하기 위한 최소의 0의 개수
if route < m + n - 1:
    print(-1)
    sys.exit()

#wall_comb = list(combinations(wall_list, len(wall_list)-1))

#graph_copy = [ [0 for i in range(m)] for j in range(n)]

#이동할 방향을 정의(상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited_ = [[False for i in range(m)] for j in range(n)]
def bfs(x, y):
    queue = deque()
    queue.append( (x, y) )
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        if visited[n-1][m-1]:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx>=n or ny >=m:
                continue

            if graph[nx][ny] == 1:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                visited[nx][ny] = True
                queue.append((nx,ny))

    #if visited[n-1][m-1]:
    #    return graph[n-1][m-1]

cnt_list = []

for x, y in wall_list:
    visited = copy.deepcopy(visited_)
    graph = copy.deepcopy(graph_)
    graph[x][y] = 0
    bfs(0, 0)
    if visited[n-1][m-1]:
        cnt_list.append(graph[n-1][m-1])

#print(cnt_list)
if (max(cnt_list) == 0):
    print(-1)
else:
    print(max(cnt_list)+1)

"""

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = [ list(map(int, sys.stdin.readline().rstrip())) for i in range(n)]
#상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    queue = deque()
    queue.append([0, 0, 1])
    #x,y좌표,벽을 뚫을 수 있는 상태(0이면 뚫을 기회 사용, 1이면 뚫을 기회 있음)
    visit = [[[0] * 2 for i in range(m)] for i in range(n)]
    visit[0][0][1] = 1
    while queue:
        x, y, w = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visit[x][y][w]
        #4방향에 대해 동시에 탐색해서 queue에 넣기 때문에, 벽을 부수는 모든 경우의 수 고려 가능(더 빠른 경우의 수를 우선적으로 탐색하게 됨)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                #벽을 만났고, 뚫을수 있는 기회가 있는 경우
                if graph[nx][ny] == 1 and w == 1:
                    visit[nx][ny][0] = visit[x][y][1] + 1
                    queue.append([nx, ny, 0])
                #벽을 한번 뚫은 경우에는 벽이 아닌 곳들만 탐색
                elif graph[nx][ny] == 0 and visit[nx][ny][w] == 0:
                    visit[nx][ny][w] = visit[x][y][w] + 1
                    queue.append([nx, ny, w])

    return -1

print(bfs())
'''
[[3, 1], [2, 0], [3, 0], [4, 0]]
[[2, 0], [0, 0], [0, 0], [5, 0]]
[[0, 0], [8, 0], [7, 0], [6, 0]]
[[10, 0], [9, 0], [8, 0], [7, 0]]
[[11, 0], [0, 0], [0, 0], [0, 0]]
[[12, 0], [13, 0], [14, 0], [15, 0]]
'''

