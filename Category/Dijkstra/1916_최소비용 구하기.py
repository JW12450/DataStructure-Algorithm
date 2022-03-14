import sys, heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[]for i in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))

start, end = map(int, sys.stdin.readline().split())
INF = 10e9
distance = [INF for i in range(n+1)]

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

print(distance[end])