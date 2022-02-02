import sys
from collections import deque

n = int(sys.stdin.readline())
#graph = [  for i in range(n)]
graph = [[] for i in range(n)]

for i in range(n):
    input = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if input[j] == 1:
            graph[i].append(j)
#스택 오버플로우 ㅜ
def dfs(graph, start, end, visited):

    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, end, visited)

    if visited[end] == True:
        return True
    else:
        return False

def bfs(graph, start, end, visited):
    queue = deque([start])

    #visited[start] = True

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    if visited[end] == True:
        return True
    else:
        return False

ans = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        visited = [False] * n
        if bfs(graph, i, j, visited):
            ans[i][j] = 1

for i in range(n):
    for j in range(n):
        print(ans[i][j],end = ' ')
    print()

