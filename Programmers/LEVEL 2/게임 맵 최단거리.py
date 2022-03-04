from collections import deque


def solution(graph):
    n = len(graph)
    m = len(graph[0])
    visited = [[False for i in range(m)] for j in range(n)]

    # 상하좌우 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m and graph[nx][ny] != 0 and visited[nx][ny] == False:
                graph[nx][ny] = graph[x][y] + 1
                visited[nx][ny] = True
                queue.append((nx, ny))

    if not visited[n - 1][m - 1]:
        return -1
    else:
        return graph[n - 1][m - 1]