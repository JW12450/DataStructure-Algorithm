import sys
n = int(sys.stdin.readline())

ans = 0
#퀸이 놓여지는 위치 [i][j] -> row[i]=j
row = [0] * n

def is_promising(x):
    for i in range(x):
        #놓인 위치를 기준으로 같은열에 이미 놓여진 퀸이 있는 경우 / 왼쪽 대각선, 오른쪽 대각선에 이미 놓여진 퀸이 있는 경우
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            # [x, i]에 퀸 배치
            row[x] = i
            #해당 위치에 놓는 것이 가능한 경우
            if is_promising(x):
                n_queens(x + 1)


n_queens(0)
print(ans)