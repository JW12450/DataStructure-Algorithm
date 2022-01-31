from collections import deque
import sys

n = int(sys.stdin.readline())

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

visited = [ [False for i in range(n)] for  j in range(n)]

#행렬 상에서의 이동 기준 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 2
def bfs(x, y):
    global count

    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    graph[x][y] = count

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx>=n or ny >=n:
                continue

            if graph[nx][ny] == 0:
                continue

            #처음 방문하는 노드인 경우
            if graph[nx][ny] == 1:
                graph[nx][ny] = count
                visited[nx][ny] = True
                queue.append((nx, ny))

    count += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0 and visited[i][j] == False:
            bfs(i, j)

all = []
for i in range(n):
    for j in range(n):
        all.append(graph[i][j])

all_set = set(all)


list_all = list(all_set)
if list_all[0] == 2:
    print(1)
    print(n*n)
else:
    print(len(set(all)) - 1)

final_list = []
for i in range(1, len(all_set)):
    final_list.append(all.count(list_all[i]))

final_list.sort()

for i in range(len(final_list)):
    print(final_list[i])
