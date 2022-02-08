import sys, copy
from itertools import combinations
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [ list(map(int, sys.stdin.readline().split())) for i in range(n)]

wall_list = []
wall_candidate = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            wall_list.append( (i, j) )
        if graph[i][j] == 0:
            wall_candidate.append( (i, j) )

wall_comb = list(combinations(wall_candidate, 3))
#이동할 방향을 정의(상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, x, y):
    global visited
    queue = deque()
    queue.append( (x, y) )

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == 1:
                continue

            if graph[nx][ny] == 0:
                visited[nx][ny] = True
                graph[nx][ny] = 2
                queue.append( (nx, ny))

safe_zone = []
for comb in wall_comb:
    graph_ = copy.deepcopy(graph)
    for i in range(3):
        #print(graph_)
        x, y = comb[i]
        graph_[x][y] = 1

    visited = [[False for i in range(m)] for j in range(n)]
    sum = 0
    for x in range(n):
        for y in range(m):
            if not visited[x][y] and graph_[x][y] == 2:
                bfs(graph_, x, y)

    for i in range(n):
        for j in range(m):
            if graph_[i][j] == 0:
                sum += 1

    #for g in graph_:
    #    print(g)
    #print(sum)
    safe_zone.append(sum)
    """
    for g in graph_:
        print(g)
    print()
    """

print(max(safe_zone))