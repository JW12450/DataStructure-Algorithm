import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [ list(sys.stdin.readline().rstrip()) for i in range(n)]

#좌표 기준 상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [ [False for i in range(n)] for j in range(n) ]

def dfs_blue(x, y):
    queue = deque()
    queue.append( (x, y ))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx>=n or ny>=n:
                continue
            if graph[nx][ny] == 'R' or graph[nx][ny] == 'G':
                continue
            if graph[nx][ny] == 'B' and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append( (nx, ny) )

def dfs_red(x, y):
    queue = deque()
    queue.append( (x, y ))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx>=n or ny>=n:
                continue
            if graph[nx][ny] == 'B' or graph[nx][ny] == 'G':
                continue
            if graph[nx][ny] == 'R' and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append( (nx, ny) )

def dfs_green(x, y):
    queue = deque()
    queue.append( (x, y ))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx>=n or ny>=n:
                continue
            if graph[nx][ny] == 'R' or graph[nx][ny] == 'B':
                continue
            if graph[nx][ny] == 'G' and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append( (nx, ny) )

def dfs_redgreen(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == 'B' :
                continue
            if (graph[nx][ny] == 'R' or graph[nx][ny] == 'G') and visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx, ny))
r_cnt = 0
g_cnt = 0

for x in range(n):
    for y in range(n):
        if not visited[x][y]:
            if graph[x][y] == 'R':
                dfs_red(x, y)
                r_cnt += 1
            if graph[x][y] == 'G':
                dfs_green(x, y)
                g_cnt += 1

visited = [ [False for i in range(n)] for j in range(n) ]
b_cnt = 0
rg_cnt = 0
for x in range(n):
    for y in range(n):
        if not visited[x][y]:
            if graph[x][y] == 'B':
                dfs_blue(x, y)
                b_cnt += 1
            if graph[x][y] == 'R' or graph[x][y] == 'G':
                dfs_redgreen(x, y)
                rg_cnt += 1

print(r_cnt + g_cnt + b_cnt, end=' ')
print(b_cnt + rg_cnt)