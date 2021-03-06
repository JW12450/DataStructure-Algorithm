import math, sys

n = int(sys.stdin.readline())
desk = [[0 for i in range(n)]for j in range(n)]
array = [[]for i in range(n*n + 1)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#1번 조건 인접한 칸 중에 비어있는 칸이 가장 많은 칸으로 이동 : 주변에 좋아하는 학생이 많이 인접해 있는 칸을 찾는 함수
def find_fav():
    max_fav = 0
    cand_fav = []
    for x in range(n):
        for y in range(n):
            if desk[x][y] != 0:
                continue
            cnt = 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                # 조건을 벗어나는 경우
                if 0 <= nx < n and 0 <= ny < n and desk[nx][ny] in array[num]:
                    cnt += 1
            if cnt > max_fav:
                max_fav = cnt
                cand_fav = []
                cand_fav.append((x,y))
            elif cnt == max_fav:
                cand_fav.append((x, y))
    return cand_fav

#2번 조건: 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
def find_empty():
    max_empty = 0
    cand_empty = []
    for c in cand_fav:
        x, y = c[0], c[1]
        if desk[x][y] != 0:
            continue
        cnt = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and desk[nx][ny] == 0:
                cnt += 1
        if cnt > max_empty:
            cand_empty = []
            cand_empty.append((x, y))
            max_empty = cnt
        elif cnt == max_empty:
            cand_empty.append((x, y))

    return cand_empty

for _ in range(n*n):
    num, a,b,c,d = map(int, sys.stdin.readline().split())
    array[num] = [a,b,c,d]
    cand_fav = find_fav()

    if len(cand_fav) == 1:
        x, y = cand_fav[0][0], cand_fav[0][1]
        desk[x][y] = num
    else:
        cand_empty = find_empty()
        x, y = cand_empty[0][0], cand_empty[0][1]
        desk[x][y] = num

#for d in desk:
#    print(d)
ans = 0
for x in range(n):
    for y in range(n):
        cnt = 0
        num = desk[x][y]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and desk[nx][ny] in array[num]:
                cnt += 1
        if cnt > 0:
            ans += math.pow(10, cnt-1)
print(int(ans))