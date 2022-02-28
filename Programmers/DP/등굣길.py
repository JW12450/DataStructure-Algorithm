from collections import deque


def solution(m, n, puddles):
    answer = 0
    graph = [[0 for i in range(m)] for j in range(n)]
    graph[0][0] = 1

    for x, y in puddles:
        graph[y - 1][x - 1] = -1

    dx = [1, 0]
    dy = [0, 1]

    queue = deque()
    queue.append((0, 0))
    while queue:
        x, y = queue.popleft()

        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < n and ny < m and graph[nx][ny] != -1:
                queue.append((nx, ny))
                graph[nx][ny] = (graph[nx][ny] + 1) % 1000000007

    return graph[-1][-1]