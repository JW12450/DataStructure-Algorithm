from sys import stdin
from collections import deque


def visitable(x, y, w):
    return 0 <= x < n and 0 <= y < m and not visited[x][y][w]


def bfs(start):
    q = deque([start])
    dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))

    while q:
        cur_x, cur_y, wall = q.popleft()
        dist = visited[cur_x][cur_y][wall] + 1

        if [cur_x, cur_y] == [n - 1, m - 1]:
            return visited[cur_x][cur_y][wall]

        for x, y in dirs:
            next_x, next_y = cur_x + x, cur_y + y
            if visitable(next_x, next_y, wall):
                if not graph[next_x][next_y]:
                    visited[next_x][next_y][wall] = dist
                    q.append((next_x, next_y, wall))
                elif wall < k:
                    visited[next_x][next_y][wall + 1] = dist
                    q.append((next_x, next_y, wall + 1))

    return -1


if __name__ == '__main__':
    n, m, k = map(int, stdin.readline().split())
    graph = [list(map(int, stdin.readline().strip())) for _ in range(n)]
    visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]
    visited[0][0] = [1] * (k + 1)
    print(bfs((0, 0, 0)))