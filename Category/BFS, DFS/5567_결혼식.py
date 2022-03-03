import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[]for i in range(n+1)]
for i in range(m):
    a, b= map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] *(n+1)

def dfs(graph, start, visited):
    visited[start] = True
    for v in graph[start]:
        if not visited[v]:
            visited[v] = True
            dfs(graph, v, visited)

def bfs(graph, start, visited):
    queue = deque([start])

    visited[start] = 0

    while queue:
        v = queue.popleft()
        #print(visited)
        for i in graph[v]:
            if visited[i] != 0:
                continue
            else:
                visited[i] = visited[v] + 1
                queue.append(i)

bfs(graph, 1, visited)


cnt = 0
for i in range(2, n+1):
    if 1<= visited[i] <= 2:
        cnt += 1
print(cnt)
