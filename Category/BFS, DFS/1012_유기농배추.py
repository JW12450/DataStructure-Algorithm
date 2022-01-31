import sys
from collections import deque

t = int(sys.stdin.readline())

#행렬 상에서의 이동 기준 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check():
    #m:가로길이       n:세로길이        k:배추가 심어져 있는 위치의 개수
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0 for i in range(m)] for j in range(n)]

    for i in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1

    visited = [[False for i in range(m)] for j in range(n)]
    cnt = 0

    for x in range(n):
        for y in range(m):
            if graph[x][y] == 1 and visited[x][y] == False:
                bfs(x, y, graph, visited, m, n)
                cnt += 1
    return cnt

def bfs(x,y, graph, visited, m, n):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue

            # 처음 방문하는 노드인 경우
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx, ny))

for _ in range(t):
    print(check())