import sys

n, m, x, y, k = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
command = list(map(int, sys.stdin.readline().rstrip().split()))

#인덱스0 이 바닥, 동, 서, 북, 남, 6이 윗면
dice = [0 for _ in range(6)]

#이동 방향 동, 서, 북, 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(k):
    d = command[i] -1
    nx = x + dx[d]
    ny = y + dy[d]

    if nx < 0 or nx>= n or ny < 0 or ny >= m:
        continue

    #동쪽으로 굴렸을때를 기준으로 주사위 조정
    if d == 0:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    #서쪽
    elif d == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    #북쪽
    elif d == 2:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    #남쪽
    else:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[5]
    else:
        dice[5] = graph[nx][ny]
        graph[nx][ny] = 0

    x, y = nx, ny
    print(dice[0])