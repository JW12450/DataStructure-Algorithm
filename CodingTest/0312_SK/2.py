from collections import deque


def bfs_t(ans, visited, n):
    queue = deque()
    loop = 0
    start = 1
    if n % 2 == 0:
        loop = n // 2
    else:
        loop = n // 2 + 1
    for i in range(loop):
        queue.append((i, i))
        queue.append((i, n - 1 - i))
        queue.append((n - 1 - i, n - 1 - i))
        queue.append((n - 1 - i, i))
        visited[i][i] = True
        visited[i][n - 1 - i] = True
        visited[n - 1 - i][n - 1 - i] = True
        visited[n - 1 - i][i] = True
        ans[i][i] = start
        ans[i][n - 1 - i] = start
        ans[n - 1 - i][n - 1 - i] = start
        ans[n - 1 - i][i] = start

        while queue:
            # 다음 좌표
            # 이동 우선 순위 오른쪽, 아래, 왼쪽, 위
            x, y = queue.popleft()
            if 0 <= x < n and 0 <= y + 1 < n and visited[x][y + 1] == False:
                ans[x][y + 1] = ans[x][y] + 1
                visited[x][y + 1] = True
                queue.append((x, y + 1))

            x, y = queue.popleft()
            if 0 <= x + 1 < n and 0 <= y < n and visited[x + 1][y] == False:
                ans[x + 1][y] = ans[x][y] + 1
                visited[x + 1][y] = True
                queue.append((x + 1, y))

            x, y = queue.popleft()
            if 0 <= x < n and 0 <= y - 1 < n and visited[x][y - 1] == False:
                ans[x][y - 1] = ans[x][y] + 1
                visited[x][y - 1] = True
                queue.append((x, y - 1))

            x, y = queue.popleft()
            if 0 <= x - 1 < n and 0 <= y < n and visited[x - 1][y] == False:
                ans[x - 1][y] = ans[x][y] + 1
                visited[x - 1][y] = True
                queue.append((x - 1, y))

        start = ans[x][y] + 1


def bfs_f(ans, visited, n):
    queue = deque()
    loop = 0
    start = 1
    if n % 2 == 0:
        loop = n // 2
    else:
        loop = n // 2 + 1
    for i in range(loop):
        queue.append((i, i))
        queue.append((i, n - 1 - i))
        queue.append((n - 1 - i, n - 1 - i))
        queue.append((n - 1 - i, i))
        visited[i][i] = True
        visited[i][n - 1 - i] = True
        visited[n - 1 - i][n - 1 - i] = True
        visited[n - 1 - i][i] = True
        ans[i][i] = start
        ans[i][n - 1 - i] = start
        ans[n - 1 - i][n - 1 - i] = start
        ans[n - 1 - i][i] = start

        while queue:
            # 다음 좌표
            # 이동 우선 순위 오른쪽, 아래, 왼쪽, 위
            x, y = queue.popleft()
            if 0 <= x + 1 < n and 0 <= y < n and visited[x + 1][y] == False:
                ans[x + 1][y] = ans[x][y] + 1
                visited[x + 1][y] = True
                queue.append((x + 1, y))

            x, y = queue.popleft()
            if 0 <= x < n and 0 <= y - 1 < n and visited[x][y - 1] == False:
                ans[x][y - 1] = ans[x][y] + 1
                visited[x][y - 1] = True
                queue.append((x, y - 1))

            x, y = queue.popleft()
            if 0 <= x - 1 < n and 0 <= y < n and visited[x - 1][y] == False:
                ans[x - 1][y] = ans[x][y] + 1
                visited[x - 1][y] = True
                queue.append((x - 1, y))

            x, y = queue.popleft()
            if 0 <= x < n and 0 <= y + 1 < n and visited[x][y + 1] == False:
                ans[x][y + 1] = ans[x][y] + 1
                visited[x][y + 1] = True
                queue.append((x, y + 1))

        start = ans[x][y] + 1


def solution(n, clockwise):
    ans = [[0 for j in range(n)] for i in range(n)]
    cnt = 0
    visited = [[False for i in range(n)] for j in range(n)]
    if clockwise:
        bfs_t(ans, visited, n)
    else:
        bfs_f(ans, visited, n)

    return ans