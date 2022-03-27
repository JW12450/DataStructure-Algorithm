import sys, copy

r, c, t = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(r)]
#한 타임때 빈공간에 확산되는 미세먼지를 담아둘 배열
save = [[[]for i in range(c)]for j in range(r)]

#상 하 좌 우 이동방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dust_move(graph, x, y):
    dust = graph[x][y]
    move = graph[x][y]//5
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < r and 0<= ny < c and graph[nx][ny] != -1:
            cnt += 1
            save[nx][ny].append(move)

    graph[x][y] = dust - move*cnt

def sum_dust(graph):
    for x in range(r):
        for y in range(c):
            if len(save[x][y]) > 0:
                graph[x][y] += sum(save[x][y])
                save[x][y] = []

def clean_dust(graph):
    graph_ = copy.deepcopy(graph)
    c1 = cleaner[0][0]
    c2 = cleaner[1][0]
    graph_[c1][1] = 0
    graph_[c2][1] = 0
    #->
    for i in range(2,c):
        graph_[c1][i] = graph[c1][i-1]
        graph_[c2][i] = graph[c2][i - 1]
    #위
    for i in range(c1-1, -1, -1):
        graph_[i][c-1] = graph[i+1][c-1]
    #아래
    for i in range(c2+1, r):
        graph_[i][c-1] = graph[i-1][c-1]
    # <-
    for i in range(c-2,-1,-1):
        graph_[0][i] = graph[0][i+1]
        graph_[r-1][i] = graph[r-1][i+1]
    #아래
    for i in range(1,c1):
        graph_[i][0] = graph[i-1][0]
    #위
    for i in range(r-2, c2, -1):
        graph_[i][0] =graph[i+1][0]
    return graph_

cleaner = []
for i in range(r):
    if graph[i][0] == -1:
        cleaner.append([i, 0])

for _ in range(t):
    for x in range(r):
        for y in range(c):
            if graph[x][y] == -1 or graph[x][y] == 0:
                continue
            dust_move(graph, x, y)

    sum_dust(graph)
    graph = clean_dust(graph)

ans = 0
for x in range(r):
    for y in range(c):
        if graph[x][y] != -1:
            ans += graph[x][y]

print(ans)
