import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(n)]
visited = [[False for i in range(m)] for j in range(n)]

def bfs(graph, start, visited):
    queue = deque([start])
    queue.append((start))
    #visited[0][0] = True
    #방향 이동 아래, 오른쪽, 대각선
    dx = [1, 0, 1]
    dy = [0, 1, 1]

    #현재 위치로 올수있던 이전 좌표의 후보들
    #위, 왼쪽, 대각선 위
    fx = [-1, 0, -1]
    fy = [0, -1, -1]

    while queue:
        x, y = queue.popleft()
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
                cand = []
                for j in range(3):
                    ffx = nx + fx[j]
                    ffy = ny + fy[j]
                    if 0 <= ffx < n and 0 <= ffy < m:
                        cand.append(graph[ffx][ffy])
                graph[nx][ny] += max(cand)
                visited[nx][ny] = True
                queue.append((nx, ny))

start = (0,0)
bfs(graph, start, visited)
print(graph[n-1][-1])