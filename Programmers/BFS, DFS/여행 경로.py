def dfs(graph, start, answer, visited, city, tickets):
    for i in graph[start]:
        if visited[start][i] > 0:
            visited[start][i] -= 1
            answer.append(city[i])
            dfs(graph, i, answer, visited, city, tickets)
            if len(answer) < len(tickets) + 1:
                answer.pop()
                visited[start][i] += 1


def solution(tickets):
    answer = []
    t = set()
    for a in tickets:
        t.add(a[0])
        t.add(a[1])

    cand = list(t)
    cand.sort(key=lambda x: (x[0], x[1], x[2]))

    city = {}
    for i in range(len(cand)):
        city[cand[i]] = i
        city[i] = cand[i]

    graph = [[] for i in range(len(cand))]
    visited = [[0 for j in range(len(cand))] for i in range(len(cand))]

    for t in tickets:
        current, next = t[0], t[1]
        graph[city[current]].append(city[next])
        visited[city[current]][city[next]] += 1

    for g in graph:
        g.sort()

    start = city["ICN"]
    cnt = 1
    answer.append(city[start])
    dfs(graph, start, answer, visited, city, tickets)

    return (answer)