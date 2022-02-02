import sys, copy
from collections import deque

n = int(sys.stdin.readline())
graph_ = [ list(map(int, sys.stdin.readline().split())) for i in range(n)]
#이동할 방향을 정의(상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global graph, rain

    queue = deque()
    queue.append( (x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx>=n or ny >=n:
                continue

            if graph[nx][ny] <= rain:
                continue

            if graph[nx][ny] > rain and visited[nx][ny] == False:
                #graph[nx][ny] =
                visited[nx][ny] = True
                queue.append((nx, ny))

sum_list=[]
#침수 기준의 높이는 1이상 100이하, 비가 2만큼오면 2까지 잠김
for rain in range(0, 101):
    visited =[[ False for i in range(n)] for j in range(n)]
    graph = copy.deepcopy(graph_)
    cnt = 0
    for x in range(n):
        for y in range(n):
            #높이 i가 침수의 기준일때 침수되지 않은 곳
            if not visited[x][y] and graph[x][y] > rain:
                bfs(x,y)
                cnt += 1

    #print('강수량 :', rain)
    #print(cnt)
    #for g in graph:
    #    print(g)
    #for v in visited:
    #    print(v)
    #print()
    sum_list.append(cnt)

print(max(sum_list))


