import sys
sys.setrecursionlimit(10**9)
n = int(sys.stdin.readline())
graph = [[]for i in range(n+1)]

for i in range(n-1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

#for i in range(n+1):
#    graph[i].sort()

def dfs(graph, v, visited):
    visited[v] = True
    #print(visited)
    #print(graph[v])
    for i in graph[v]:
        if parent[i] == 0:
            parent[i] = v
        if not visited[i]:
            dfs(graph, i, visited)


visited = [False]*(n+1)
parent = [0]*(n+1)
dfs(graph, 1, visited)

for i in range(2, n+1):
    print(parent[i])