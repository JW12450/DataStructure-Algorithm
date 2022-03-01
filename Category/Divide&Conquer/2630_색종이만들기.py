import sys

n = int(sys.stdin.readline())
array = []
for i in range(n):
    array.append(list(map(int, sys.stdin.readline().split())))
#전체 종이의 크기는 n * n

white = 0
blue = 0
def square_check(x, y, n):
    global blue, white
    check = array[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check!= array[i][j]:
                square_check(x, y, n // 2)  # 1사분면
                square_check(x, y + n // 2, n // 2)  # 2사분면
                square_check(x + n // 2, y, n // 2)  # 3사분면
                square_check(x + n // 2, y + n // 2, n // 2)  # 4사분면
                return

    if check == 0:
        white += 1
        return
    else:
        blue += 1
        return

square_check(0, 0, n)

print(white)
print(blue)