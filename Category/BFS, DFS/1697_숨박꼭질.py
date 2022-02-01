"""
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

graph = []
for i in range(100001):
    inner_list = []
    if i-1 >= 0 and i-1 <=100000:
        inner_list.append(i-1)
    if i+1 >= 0 and i+1 <= 100000:
        inner_list.append(i+1)
    if i*2 >= 0 and i*2 <= 100000:
        inner_list.append(2 * i)

    graph.append(inner_list)
#print(graph)
if n > k:
    print(n-k)
    sys.exit()

visited = [False] * (100001)
count = 0

def bfs(graph, start, visited):
    global count, k
    queue = deque([start])
    visited[start] = True

    cnt_loop = queue[-1]
    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if i >= 0 and i < 100001 and visited[i] == False:
                queue.append(i)
                visited[i] = True
                if visited[k]:
                    return count
        if v == cnt_loop:
            count += 1
            cnt_loop = queue[-1]
        #print(queue, count)

print(bfs(graph, n, visited)+1)
"""




import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
visited = [False] * (100001)
dist = [0] * (100001)

def bfs():
    queue = deque()
    queue.append(n)

    while queue:
        x = queue.popleft()
        if x == k:
            print(dist[x])
            break

        for nx in (x-1, x+1, 2*x):
            if 0 <= nx <= 100000 and not dist[nx]:
                dist[nx] = dist[x] + 1
                queue.append(nx)

bfs()