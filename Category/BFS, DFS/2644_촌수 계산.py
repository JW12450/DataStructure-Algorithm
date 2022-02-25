import sys
from collections import deque
sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())

m = int(sys.stdin.readline())
graph = [[]for i in range(n+1)]
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

chon = [-1]*(n+1)
visited = [False]*(n+1)

def bfs(graph, start, visited):
    queue = deque([start])

    visited[start] = True
    chon[start] = 0
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                chon[i] = chon[v] + 1

bfs(graph, a, visited)
#print(chon)
print(chon[b])

"""
if visited[b] == False:
    print(-1)
else:
    print(chon[b])
"""
