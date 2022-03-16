import sys, heapq


n, e = map(int, sys.stdin.readline().split())
graph = [[]for i in range(n+1)]

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1, v2 = map(int, sys.stdin.readline().split())

inf = int(1e9)

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance = [inf] * (n + 1)
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

    return distance

one = dijkstra(1)
v1_d = dijkstra(v1)
v2_d = dijkstra(v2)

v1_path = one[v1] + v1_d[v2] + v2_d[n]
v2_path = one[v2] + v2_d[v1] + v1_d[n]

result = min(v1_path, v2_path)
if result < inf:
    print(result)
else:
    print(-1)
