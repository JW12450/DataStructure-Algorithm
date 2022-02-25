import sys
from collections import deque

def knight_move(n, current, target):
    graph = [[0 for i in range(n)]for j in range(n)]

    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]

    queue = deque()
    queue.append(current)

    while queue:
        x, y = queue.popleft()
        if x == target[0] and y==target[1]:
            return graph[x][y]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx>=n or ny >=n:
                continue
            if graph[nx][ny] != 0:
                continue
            else:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])




t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    current = list(map(int, sys.stdin.readline().rstrip().split()))
    target = list(map(int, sys.stdin.readline().rstrip().split()))
    print(knight_move(n, current, target))