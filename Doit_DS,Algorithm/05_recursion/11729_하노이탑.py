import sys

n = int(sys.stdin.readline())

result = []

def move(count, num, x, y) -> None:
    if num > 1:
        count +=1
        move(count, num-1, x, 6-x-y)

    result.append([x,y])

    if num > 1:
        count += 1
        move(count, num-1, 6-x-y, y)

count = 0
move(count, n, 1, 3)
print(len(result))
for i in range(len(result)):
    for j in range(2):
        print(result[i][j], end=" ")
    print()