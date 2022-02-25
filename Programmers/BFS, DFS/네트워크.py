from collections import deque


def dfs(graph, start, visited):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)


def solution(n, computers):
    answer = 0
    graph = [[] for i in range(n + 1)]
    for i, c in enumerate(computers):
        for j in range(1, len(c) + 1):
            if c[j - 1] == 1:
                graph[i + 1].append(j)

    visited = [False] * (n + 1)

    cnt = 0
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(graph, i, visited)
            cnt += 1

    return cnt