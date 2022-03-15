import sys

n, m, b = map(int, sys.stdin.readline().split())
#graph = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
graph = []
for i in range(n):
    g = list(map(int, sys.stdin.readline().split()))
    for gg in g:
        graph.append(gg)


def find(graph, h, b):
    time = 0
    for g in graph:
        if g > h:
            b += g - h
            time += (g - h) * 2
        else:
            b -= h - g
            time += (h - g)
    """
    for x in range(n):
        for y in range(m):
            if graph[x][y] == h:
                continue
            elif graph[x][y] > h:
                b += graph[x][y] - h
                time += (graph[x][y] - h) * 2
            else:
                b -= h - graph[x][y]
                time += (h - graph[x][y])
    """

    if b < 0:
        time = -1
    return time

#높이 완탐
min_time = 987654321

min_h = 0
for h in range(257):
    tmp = b
    time = find(graph, h, tmp)
    if time <0:
        continue
    elif time <= min_time:
        min_time = time
        min_h = h
        #print(min_time, min_h)
    else:
        break

print(min_time, min_h)

"""
반례
// 350 45
2 2 35
20 10
190 40


// 290 170
2 2 68
120 90
250 170
"""