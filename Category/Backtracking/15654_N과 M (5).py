n,m = map(int, input().split())
array = list(map(int, input().split()))

array.sort()
s = []
visited = [False] * (array[-1] + 1)

def dfs():
    if len(s) == m:
        print(" ".join(map(str, s)))
        return
    for a in array:
        if visited[a]:
            continue
        visited[a] = True
        s.append(a)
        dfs()
        visited[a] = False
        s.pop()

dfs()
