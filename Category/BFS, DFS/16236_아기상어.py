import sys

n = int(sys.stdin.readline())

graph = [list(map(int, sys.stdin.readline().rstrip().split()))for _ in range(n)]

for g in graph:
    print(g)

