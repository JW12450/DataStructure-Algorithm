import sys

n = int(sys.stdin.readline())

result = []
count = 0
#원판의 갯수, 시작기둥, 목표기둥
def move(num, x, y) :
    global count
    #가장 바닥에 있는 원반을 제외한 그 위의 그룹들을 시작기둥에서 중간기둥으로 옮김
    if num > 1:
        move(num-1, x, 6-x-y)

    #가장 바닥의 기둥을 시작기둥에서 목표기둥으로 옮김
    #print(f'원반 {num} 을 {x}기둥에서 {y}기둥')
    count += 1
    result.append([x,y])

    #가장 바닥에 있는 원반을 제외한 그 위의 그룹들을 중간기둥에서 목표기둥으로 옮김
    if num > 1:
        move(num-1, 6-x-y, y)


move(n, 1, 3)

print(count)

for i in range(len(result)):
    for j in range(2):
        print(result[i][j], end=" ")
    print()