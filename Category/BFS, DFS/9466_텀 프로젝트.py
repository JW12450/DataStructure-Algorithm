import sys
sys.setrecursionlimit(111111)

t = int(sys.stdin.readline())


def dfs(i):
    global result
    visited[i] = True
    cycle.append(i)
    number = numbers[i]

    if visited[number]:
        if number in cycle:
            result += cycle[cycle.index(number):]
        return
    else:
            dfs(number)

for _ in range(t):
    n = int(sys.stdin.readline())
    numbers = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
    visited = [True] + [False]*n
    result = []

    for i in range(1,n+1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(n - len(result))



"""
import copy
import sys

t = int(sys.stdin.readline())

def dfs(graph, visited, start, now):
    visited[start] = True
    for i in graph[start]:
        if i == now:
            return True
        if not visited[i]:
            dfs(graph, visited,i, now)
    return False
for _ in range(t):
    n = int(sys.stdin.readline())
    table = list(map(int, sys.stdin.readline().rstrip().split()))
    graph = [[]for i in range(n+1)]
    for i in range(1,n+1):
        if table[i-1] not in graph[i]:
            graph[i].append(table[i-1])
        if i not in graph[table[i-1]]:
            graph[table[i-1]].append(i)
    for g in graph:
        print(g)
    visited = [False]*(n+1)
    visited_copy = copy.deepcopy(visited)
    cnt = 0
    for i in range(1,n+1):
        if not visited[i]:
            if dfs(graph, visited_copy, i, i):
                cnt += 1
                visited = visited_copy
            print(visited)

    print(cnt)

"""