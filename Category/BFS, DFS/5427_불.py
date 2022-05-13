import sys
from collections import deque

t = int(sys.stdin.readline())
#상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#1초마다 인접한 빈공간으로 불이 퍼짐 -> 상근이가 이동
#따라서, 초단위 기준으로 불의 bfs, 상근이의 bfs를 한큐씩 돌림
def fire():
    for _ in range(len(fire_queue)):
        x, y = fire_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #범위 안의 빈공간만 불이 퍼져나감
            if (0 <= ny < w and 0 <= nx < h) and graph[nx][ny] == ".":
                graph[nx][ny] = "*"
                fire_queue.append((nx, ny))

def move(start_x, start_y):
    queue = deque()
    queue.append([start_x, start_y])

    while queue:
        #1초 기준 큐에 있는 이동가능한 지점들을 모두 탐색해봐야 하기 때문에 while문 내부에서 for문
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                #탈출에 성공한 경우
                if (nx<0 or nx>= h) or (ny < 0 or ny>= w):
                    return visited[x][y] + 1
                else:
                    if 0<=nx<h and 0<=ny<w and visited[nx][ny] == 0 and graph[nx][ny] == ".":
                        queue.append((nx, ny))
                        visited[nx][ny] = visited[x][y] + 1
        fire()
        #for g in graph:
        #    print(g)
        #for v in visited:
        #    print(v)
        #print()
    return "IMPOSSIBLE"

def solve():
    global w,h, graph, fire_queue, visited
    w, h = map(int, sys.stdin.readline().split())
    graph = []
    visited = [[0] * w for _ in range(h)]

    for _ in range(h):
        graph.append(list(str(sys.stdin.readline().rstrip())))
    #불의 확산 지점들을 넣는 큐
    fire_queue = deque()

    for x in range(h):
        for y in range(w):
            if graph[x][y] == "@":
                start_x, start_y = x, y
            if graph[x][y] == "*":
                fire_queue.append((x,y))

    fire()
    print(move(start_x,start_y))

for _ in range(t):
    solve()

