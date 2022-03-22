import sys

n = int(sys.stdin.readline())
array = [["" for i in range(3)] for j in range(n)]

for i in range(n):
    weight, height = map(int, sys.stdin.readline().split())
    array[i] = (weight, height)

#print(array)


for i in array:
    rank = 1
    for j in array:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1

    print(rank,end=" ")
