import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int,list(input().rstrip()))) for i in range(n)]
for g in graph:
    print(g)