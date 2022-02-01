import sys
from collections import deque

#상, 하, 좌, 우, 대각선 왼쪽 위, 대각선 오른쪽위, 대각선 왼쪽 아래, 대각선 오른쪽 아래
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append( (x,y) )
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        #print(queue)
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append( (nx, ny))

temp = 1

while True:
    w, h =  map(int, sys.stdin.readline().split())

    if w == h == 0:
        break

    graph = [list(map(int, sys.stdin.readline().split())) for i in range(h)]
    visited = [[False for i in range(w)] for j in range(h)]
    cnt = 0

    for x in range(h):
        for y in range(w):
            if not visited[x][y] and graph[x][y] == 1:
                bfs(x, y)
                cnt += 1
    print(cnt)
