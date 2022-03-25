import sys

n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
#처음 주어진 방향 d를 주어진 dir에 맞게 수정
new = [3,2,1,0]
d = new[d]

def clean(graph, x, y):
    global cnt
    if graph[x][y] == 0:
        graph[x][y] = 2
        cnt += 1

#왼쪽 방향으로만 계속해서 회전함
# 서, 남, 동, 북 으로 세팅하고 막혔을 경우 다음 탐색 위치를 봄
# 서, 남, 동, 북, 서, 남, 동, 북
dx = [0, 1, 0, -1, 0, 1, 0, -1]
dy = [-1, 0, 1, 0, -1, 0 ,1, 0]
def move(graph, x, y, d):
    global cnt
    for i in range(d+1, d+5):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            graph[nx][ny] = 2
            cnt += 1
            return nx, ny, i
    #인접한 4방향에 청소할 공간이 없다면 바라보는 방향 유지한채로 한칸 후진, 이때 바라보는 방향을 유지하기 위해 저장
    tmp = d
    new = d + 2
    nx = x + dx[new]
    ny = y + dy[new]
    if not (0 <= nx < n and 0 <= ny < m) or graph[nx][ny] == 1:
        return -1, -1, d
    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
        graph[nx][ny] == 2
        cnt += 1
        x, y = nx, ny
        d = i
        return x, y, d
    elif 0 <= nx < n and 0 <= ny < m and not(graph[nx][ny] == 0):
        return nx, ny, tmp

cnt = 0
x, y = r, c
clean(graph, x, y)
dir = ["서", '남', '동', '북']
while x >0 and y >0:
    x,y,d= move(graph, x, y, d)
    d %= 4

print(cnt)
