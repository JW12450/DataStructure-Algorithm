import sys

num = int(input())
n = int(input())

graph = [ [] for i in range(num+1)]
for i in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(num+1):
    graph[i].sort()

count = 0

def dfs(graph, visited, v):
    global count
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, visited, i)
            count += 1

visited = [False] * (num+1)
print(graph)

dfs(graph, visited, 1)
print(visited)
print(count)
