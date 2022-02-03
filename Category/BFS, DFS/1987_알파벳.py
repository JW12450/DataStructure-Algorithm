import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for i in range(r)]
count = [[0 for i in range(c)] for j in range(r)]

#행렬상에서 이동 기준상 하 좌 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

visited = [False]*26

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    visited[ord( graph[x][y] ) - 65] = True
    count[x][y] += 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue

            if visited[ ord(graph[nx][ny]) - 65] :
                continue

            if not visited[ ord(graph[nx][ny]) - 65]:
                visited[ord(graph[nx][ny]) - 65] = True
                count[nx][ny] = count[x][y] + 1
                queue.append( (nx, ny))

def dfs(x, y, ans):
    global answer, visited

    answer = max(ans, answer)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # index 벗어나지 않는지 체크하고, 새로운 칸이 중복되는 알파벳인지 체크
        if ((0 <= nx < r) and (0 <= ny < c)) and (not visited[ ord(graph[nx][ny]) - 65]):
            visited[ord(graph[nx][ny]) - 65] = True
            dfs(nx, ny, ans + 1)
            # 이전 시점으로 초기화
            visited[ord(graph[nx][ny]) - 65] = False

answer = 1
visited[ ord(graph[0][0]) - 65] = True
dfs(0, 0, answer)
"""
잘못된 접근 : bfs 
bfs(0,0)

for g in count:
    print(g)
"""

print(answer)