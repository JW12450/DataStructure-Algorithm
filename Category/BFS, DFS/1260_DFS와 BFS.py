import sys
from collections import deque

# n : 정점의 개수
# m : 간선의 개수
# v : 탐색을 시작한 정점의 번호
n, m, v = map(int, sys.stdin.readline().split())

graph = [[] for i in range(n+1)]

for i in range(m):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(n+1):
    graph[i].sort()

print(graph)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])

    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False] * (n+1)
dfs(graph, v, visited)

print()
visited = [False] * (n+1)
bfs(graph, v, visited)

