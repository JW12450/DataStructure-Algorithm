import sys, heapq

n, m, x = map(int, sys.stdin.readline().split())
graph = [[]for i in range(n+1)]
for _ in range(m):
    a, b, c =  map(int, sys.stdin.readline().split())
    graph[a].append((b,c))

inf = int(1e9)
def dijstra(start):
    distance = [inf] * (n + 1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        dist, now = heapq.heappop(queue)

        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

    return distance

distance = [[]for i in range(n+1)]
for i in range(1,n+1):
    distance[i] = dijstra(i)

cand = []
for i in range(1, n+1):
    if i == x:
        continue
    cand.append(distance[i][x] + distance[x][i])

print(max(cand))