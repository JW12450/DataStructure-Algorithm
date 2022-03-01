import sys
from collections import deque


def bfs(i, j, visited, graph):
    cnt = 0
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True

    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        print(queue)
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or nx > len(graph) - 1 or ny < 0 or ny > len(graph[0]) - 1:
                continue
            if graph[nx][ny] == 0:
                continue
            if not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1
    return cnt


def getMaxField(data, n, m):
    '''
    n개의 줄에 m개의 숫자가 차례로 주어질 때, 가장 큰 잡초밭을 출력하는 함수를 작성하세요.
    '''
    ans = []
    visited = [[False for i in range(n)] for j in range(m)]
    for i in range(n):
        for j in range(m):
            if visited[i][j] == False and data[i][j] == 1:
                ans.append(bfs(i, j, visited, data))
                print(ans)
    return max(ans)


def main():
    '''
    이 부분은 수정하지 마세요.
    '''
    inputList = [int(x) for x in input().split()]

    n = inputList[0]
    m = inputList[1]
    data = [[int(x) for x in input().split()] for i in range(n)]

    print(getMaxField(data, n, m))


if __name__ == "__main__":
    main()
