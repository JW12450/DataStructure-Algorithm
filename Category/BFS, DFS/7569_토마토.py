import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())

graph = []
start_point = []
for x in range(h):
    graph.append([])
    for y in range(n):
        graph[x].append(list(map(int, sys.stdin.readline().rstrip().split())))
        for z in range(m):
            if graph[x][y][z] == 1:
                start_point.append((x,y,z))

#print(start_point)

#3차원 행렬상에서 이동 기준 : 위 아래 왼쪽 오른쪽 앞 뒤
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
def bfs():
    queue = deque()
    for i in start_point:
        queue.append( i )

    while queue:
        x, y, z = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or ny < 0 or nz < 0 or nx>=h or ny >=n or nz >= m:
                continue

            if graph[nx][ny][nz] == -1:
                continue

            if graph[nx][ny][nz] == 0:
                graph[nx][ny][nz] = graph[x][y][z] + 1
                queue.append( (nx, ny, nz) )

            #if graph[nx][ny][nz] > 1 and graph[nx][ny][nz] > (graph[nx][ny][nz]+1):
            #    graph[nx][ny][nz] = graph[nx][ny][nz] + 1
            #    queue.append((nx, ny, nz))
"""
for i in range(len(start_point)):
    x, y = start_point[i]
    bfs(x, y)
"""

bfs()

def check(graph):
    for g in graph:
        for g2 in g:
            if 0 in g2:
                return False
    return True

if not check(graph):
    print(-1)
else:
    max_list = []
    for g in graph:
        for g2 in g:
            max_list.append(max(g2))

    print(max(max_list) - 1)