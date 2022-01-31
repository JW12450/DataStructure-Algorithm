import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())

graph = []
start_point = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(len(graph[i])):
        if graph[i][j] == 1:
            start_point.append( (i, j))

#print(start_point)

#행렬상에서 이동 기준상 하 좌 우
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    queue = deque()
    for i in start_point:
        queue.append( i )

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx>=n or ny >=m:
                continue

            if graph[nx][ny] == -1:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append( (nx, ny) )

            if graph[nx][ny] > 1 and graph[nx][ny] > (graph[x][y]+1):
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
"""
for i in range(len(start_point)):
    x, y = start_point[i]
    bfs(x, y)
"""

bfs()

def check(graph):
    for g in graph:
        if 0 in g:
            return False
    return True

if not check(graph):
    print(-1)
else:
    max_list = []
    for g in graph:
        max_list.append(max(g))

    print(max(max_list) - 1)