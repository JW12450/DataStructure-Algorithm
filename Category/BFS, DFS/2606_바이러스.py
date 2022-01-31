import sys

#num = int(sys.stdin.readline())
#n = int(sys.stdin.readline())

num = int(input())
n = int(input())

graph = [ [] for i in range(num+1)]
for i in range(n):
    #x, y = map(int, sys.stdin.readline().rstrip().split())
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(num+1):
    graph[i].sort()

count = 0

def dfs(graph, visited, v):
    global count
    visited[v] = True
    #print(v, end = " ")

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, visited, i)
            count += 1

visited = [False] * (num+1)
dfs(graph, visited, 1)
print(count)

#print(graph)
#print(visited)