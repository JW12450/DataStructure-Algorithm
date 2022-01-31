"""
from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())

link_list = []
for i in range(n):
    input = list(sys.stdin.readline().rstrip())
    input_list = []
    for i in input:
        input_list.append(int(i))
    link_list.append(input_list)

#print(link_list)

graph = []
for i in range(n*m):
    link = []
    if link_list[i//m][i%m] == 1:
        if i//m < n-1:
            if link_list[i//m+1][i%m] == 1:
                link.append((i//m+1) * m + i%m)
        # 그래프의 오른쪽 노드가 존재할때
        if i % m + 1 < m:
            if link_list[i // m][i % m + 1] == 1:
                # link.append(m * i//m + i%m + 1)
                link.append(i + 1)
        # 그래프의 왼쪽 노드가 존재할때
        if i % m - 1 >= 0:
            if link_list[i // m][i % m - 1] == 1:
                # link.append(m * i//m + i%m - 1)
                link.append(i - 1)
        #그래프의 위쪽 노드가 존재할때
        if i//m > 0:
            if link_list[i//m-1][i%m] == 1:
                #link.append((i//m-1) * m + i%m)
                link.append(i-m)

    graph.append(link)

#print(graph)

visited = [False]*(n*m)
count = 0
def dfs(graph, visited, start):
    global count

    visited[start] = True
    count+=1

    if visited[n * m - 1] == True:
        print(count)

    for i in graph[start]:
        if not visited[i]:
            dfs(graph, visited, i)

#dfs(graph, visited, 0)

def bfs(graph, visited, start):
    global count
    queue = deque([start])

    visited[start] = True
    count += 1

    while queue:
        v = queue.popleft()
        #print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                count += 1
                if visited[n * m - 1] == True:
                    break


    return count

print(bfs(graph, visited, 0))
"""

from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())

graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

#이동할 방향을 정의(상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx>=n or ny >=m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

    return graph[n-1][m-1]

print(bfs(0, 0))