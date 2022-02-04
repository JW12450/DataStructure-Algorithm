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

s = [ list(map(int, sys.stdin.readline().rstrip())) for i in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs():
    q = deque()
    q.append([0, 0, 1])
    visit = [[[0] * 2 for i in range(m)] for i in range(n)]
    visit[0][0][1] = 1
    while q:
        a, b, w = q.popleft()
        if a == n - 1 and b == m - 1:
            return visit[a][b][w]
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < m:
                if s[x][y] == 1 and w == 1:
                    visit[x][y][0] = visit[a][b][1] + 1
                    q.append([x, y, 0])
                elif s[x][y] == 0 and visit[x][y][w] == 0:
                    visit[x][y][w] = visit[a][b][w] + 1
                    q.append([x, y, w])

    return -1

print(bfs())
