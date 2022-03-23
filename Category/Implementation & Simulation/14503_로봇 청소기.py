import sys

n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
#처음 주어진 방향 d를 주어진 dir에 맞게 수정
new = [3,2,1,0]
d = new[d]

#왼쪽 방향으로만 계속해서 회전함
# 서, 남, 동, 북 으로 세팅하고 막혔을 경우 다음 탐색 위치를 봄
dir = [(0,-1), (1,0), (0,1), (-1,0), (0,-1), (1,0), (0,1), (-1,0)]

def move(graph, x, y, d):
    global cnt, ans
    #현재 방향을 기준으로 왼쪽 방향부터 차례대로 인접한 칸 탐색
    d += 1
    nx = x + dir[d][0]
    ny = y + dir[d][1]
    print(cnt)
    if cnt == 4:
        x, y =  -1, -1
        return
    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
        ans += 1
        graph[nx][ny] = 1
        x, y = nx, ny
        return
    elif 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
        cnt += 1
        move(graph, x, y, d)

finish = True
ans = 0
x, y = r, c
while finish:
    cnt = 0
    move(graph, x, y, d)
    print(x, y)

print(cnt)
for g in graph:
    print(g)