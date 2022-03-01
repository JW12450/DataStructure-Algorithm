import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int,list(input().rstrip()))) for i in range(n)]
#ans = []
def square(x, y, n):
    #global ans
    check = graph[x][y]
    #print(ans)
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != graph[i][j]:
                check = -1
                break

    if check == -1:
        print("(",end="")
        square(x, y , n//2)
        square(x, y + n//2, n // 2)
        square(x + n//2, y, n // 2)
        square(x + n//2, y + n//2, n // 2)
        print(")",end="")

    elif check == 0:
        print("0",end="")
    else:
        print("1",end="")

square(0, 0, n)
#print(ans)
#print("".join(map(str,ans)))