import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for i in range(n)]
check = [[0 for i in range(n)] for j in range(n)]
ans = 0


def dfs(x, y, check):
    global ans
    # 점프 가능한 위치
    # print(x,y)
    if x == n - 1 and y == n - 1:
        ans += 1
        return
    num = graph[x][y]
    if num == 0:
        return

    # 점프칸 만큼의 아래로 이동, 오른쪽으로 이동
    dx = [num, 0]
    dy = [0, num]

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        # if nx == n-1 and ny == n-1:
        #    ans += 1
        #    return

        if nx < n and ny < n:
            dfs(nx, ny, check)


def bfs(x, y, check):
    global ans
    queue = deque()
    queue.append((0, 0))

    while queue:
        # print(queue)
        x, y = queue.popleft()

        # 점프 가능한 위치
        num = graph[x][y]
        if num == 0:
            continue

        # 점프칸 만큼의 아래로 이동, 오른쪽으로 이동
        else:
            dx = [num, 0]
            dy = [0, num]
            for i in range(2):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < n and ny < n:
                    queue.append((nx, ny))
                    check[nx][ny] += 1


bfs(0, 0, check)
# for c in check:
#    print(c)
print(check[n - 1][n - 1])
