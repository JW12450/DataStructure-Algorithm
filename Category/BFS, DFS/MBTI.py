import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for i in range(n)]
#이동 기준
# 12시방향 부터 시계방향 순
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

first = ['E', 'I']
second = ['N', 'S']
third = ['F', 'T']
fourth = ['P', 'J']
mbti = [first, second, third, fourth, []]
ans = 0

def search(graph, x, y):
    global ans
    #엠비티아이 리스트를 옮겨가면서 체크하는 포인터
    if graph[x][y] in mbti[0]:
        #print(graph[x][y], end=" ")
        for i in range(8):
            cnt = 1
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny <m and graph[nx][ny] in mbti[cnt]:
                #i는 방향 값
                #print(graph[nx][ny], end=" ")
                dfs(graph, nx, ny, i, cnt)
            #print()


def dfs(graph, x, y, i, cnt):
    global ans
    cnt += 1
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<= nx < n and 0<= ny <m and graph[nx][ny] in mbti[cnt]:
        #print(graph[nx][ny], end=" ")
        if cnt == 3:
            ans += 1
        dfs(graph, nx, ny, i, cnt)


#print(len(graph))
#print(len(graph[0]))
for x in range(n):
    for y in range(m):
        search(graph, x, y)
print(ans)

"""
Test1

5 5
JICDE
TFSFN
SESTF
EWERP
ABCDE


Test2
5 4
ENFP
ENFP
ENFP
ENFP
ENFP
"""