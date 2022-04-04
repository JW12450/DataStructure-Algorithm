import sys
from collections import deque

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
#벽 또는 자기 자신의 몸과 부딪히면 게임이 끝남 -> 벽에 닿는 조건과 현재 몸에 해당하는 좌표들을 담는 배열 필요
board = [[0 for _ in range(n+1)]for _ in range(n+1)]
for _ in range(k):
    x, y = map(int, sys.stdin.readline().split())
    board[x][y] = 1

l = int(sys.stdin.readline())
command = [0]*10001
for _ in range(l):
    time, dir = sys.stdin.readline().split()
    command[int(time)] = dir

t = 0
#좌, 상, 우, 하
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
x, y = 1, 1
#처음에는 오른쪽으로 이동
dir = 2
d = ["좌", "상", "우", "하"]
snake = deque()
snake.append((1,1))

while True:
    #해당 방향에 맞게 dir 갱신
    if command[t] == 'L':
        dir = (dir + 4 - 1)%4
    elif command[t] == 'D':
        dir = (dir + 1) % 4

    x = x + dx[dir]
    y = y + dy[dir]

    #좌표에 대한 예외처리(벽에 부딪히는 경우)를 먼저하여 인덱스에러 방지
    if 0 >= x or x> n or 0 >= y or y > n:
        break
    #머리가 먼저 이동
    snake.append((x, y))
    #뱀의 머리가 부딪히는 지 체크
    find = False
    for i, s in enumerate(snake):
        #현재 좌표는 탐색에서 제외
        if i == len(snake)-1:
            continue
        if s[0]==x and s[1]==y:
            find = True
            break
    if find:
        break
    #사과가 없으면, 꼬리 자르기 + 사과 먹었으면 갱신
    if board[x][y] == 0:
        snake.popleft()
    else:
        board[x][y] = 0

    t += 1

print(t+1)