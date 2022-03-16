import sys, heapq
input = sys.stdin.readline
from collections import deque

n, m, k, x = map(int, input().rstrip().split())
graph = [[]for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
visited = [False] * (n+1)
dist = [0]*(n+1)

def bfs(graph, visited, start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        now = queue.popleft()

        for i in graph[now]:
            if visited[i] == False:
                visited[i] = True
                dist[i] = dist[now] + 1
                queue.append(i)

bfs(graph, visited, x)
cnt = 0
for i in range(1, len(dist)):
    if dist[i] == k:
        print(i)
        cnt += 1

if cnt == 0:
    print(-1)

""""
import sys, heapq
input = sys.stdin.readline


n, m, k, x = map(int, input().rstrip().split())
graph = [[]for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append((b, 1))

inf = int(1e9)
distance = [inf] * (n+1)

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

dijkstra(x)
#print(distance)
cnt = 0
for i in range(1, len(distance)):
    if distance[i] == k:
        print(i)
        cnt += 1

if cnt == 0:
    print(-1)
"""