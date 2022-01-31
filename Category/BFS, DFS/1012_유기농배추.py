import sys
from collections import deque

input = sys.stdin.readline()

t = int(input)

def check():
    #m : 가로길이
    #n : 세로길이
    #k : 배추가 심어져 있는 위치의 개수
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0 for i in range(m)]for j in range(n)]

    for i in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1

    for j in graph:
        print(j)

for i in range(t):
    check()