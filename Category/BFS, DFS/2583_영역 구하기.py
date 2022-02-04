import sys
from collections import deque

m, n, k = map(int, sys.stdin.readline().split())
graph = [ [0 for i in range(n)] for j in range(m)]

for _ in range(k):
    a, b, c, d = map(int, sys.stdin.readline().split())
    # 0 2 4 4
    # d-b : 직사각형의 세로 길이
    # c-a : 직사각형의 가로 길이
    for i in range(m-d,m-d+(d-b)):
        for j in range(a, a+(c-a)):
            graph[i][j] = 1

#for g in graph:
#    print(g)

#이동할 방향을 정의(상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False for i in range(n)] for j in range(m)]

def bfs(x, y):
    global cnt
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    cnt += 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx>=m or ny >=n:
                continue

            if graph[nx][ny] == 1:
                continue

            if graph[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                cnt += 1
                queue.append((nx,ny))
bfs_cnt = 0
cnt_list = []
for x in range(m):
    for y in range(n):
        if not visited[x][y] and graph[x][y] == 0:
            cnt = 0
            bfs(x, y)
            cnt_list.append(cnt)
            bfs_cnt += 1

print(bfs_cnt)
cnt_list.sort()
for i in cnt_list:
    print(i, end= " ")