import sys

n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
#처음 주어진 방향 d를 주어진 dir에 맞게 수정
new = [3,2,1,0]
d = new[d]

#왼쪽 방향으로만 계속해서 회전함
# 서, 남, 동, 북 으로 세팅하고 막혔을 경우 다음 탐색 위치를 봄
# 서, 남, 동, 북, 서, 남, 동, 북
dx = [0, 1, 0, -1, 0, 1, 0, -1]
dy = [-1, 0, 1, 0, -1, 0 ,1, 0]
def move(graph, x, y, d):
    global cnt
    #현재 방향을 기준으로 왼쪽 방향부터 차례대로 인접한 칸 탐색
    for i in range(d+1, d+5):
        jump = 1
        find = True
        while find:
            nx = x + dx[i]*jump
            ny = y + dy[i]*jump
            #print("nx, ny: ", nx, ny)
            if nx < 0 or nx >= n or 0 > ny or ny >= m or graph[nx][ny] == 1:
                #print("check")
                find = False
            elif graph[nx][ny] == 0:
                #왼쪽 방향에 청소할 공간이 존재한다면 그 방향으로 회전한 다음, 한칸을 전진하고 1번부터 진행
                x, y = x + dx[i], y + dy[i]
                d = i
                return x, y, d
            else:
                jump += 1
    #네 방향 모두 돌아봤지만 청소할 공간이 없는 경우 한 칸 후진하고 2번으로
    d = d + 2
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == 0:
        graph[nx][ny] = 2
        x, y = nx, ny
        cnt += 1
        # 바라보는 방향 유지
        d -= 2
        return x, y, d
    else:
        return -1, -1, d


def clean(graph, x, y):
    global cnt
    if graph[x][y] == 0:
        graph[x][y] = 2
        cnt += 1

cnt = 0
x, y = r, c

dir = ["서", '남', '동', '북']
while x >0 and y >0:
    clean(graph, x, y)
    x,y,d = move(graph, x, y, d)
    d %= 4
    #for g in graph:
    #    print(g)
    print("현재 보고 있는 방향", dir[d])
    print("x, y :", x, y)
    print("cnt:", cnt)
    print()

print(cnt)
