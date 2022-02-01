import sys
from collections import deque

n, m =  map(int, sys.stdin.readline().split())

graph = [[] for i in range(n+1)]
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)
#print(graph)
visited = [False] * (n+1)
cnt = 0
def bfs(graph, start, visited):
    global cnt
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

for i in range(1, n+1):
    if not visited[i]:
        bfs(graph, i, visited)
        cnt += 1
        #(visited[1:])

print(cnt)