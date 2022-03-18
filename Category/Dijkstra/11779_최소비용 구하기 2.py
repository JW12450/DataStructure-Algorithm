def dijkstra(s):
    distance = [INF] * (N+1)
    distance_path = [[] for _ in range(N+1)]
    q = [[0, s, [s]]]
    distance[s] = 0

    while q:
        dist, now, path = heapq.heappop(q)

        for next_cost, next_vertex in Q[now]:
            if next_cost + dist < distance[next_vertex]:
                next_cost += dist
                distance[next_vertex] = next_cost
                distance_path[next_vertex] = path + [next_vertex]
                heapq.heappush(q, [next_cost, next_vertex, path + [next_vertex]])

    return distance, distance_path

import sys, heapq
INF = sys.maxsize

N = int(input())
M = int(input())
Q = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().split())
    Q[start].append([cost, end])

S, E = map(int, input().split())
answer, answer_path = dijkstra(S)

print(answer[E])
print(len(answer_path[E]))
for element in answer_path[E]:
    print(element, end = " ")