import sys

n = int(sys.stdin.readline())

array = []
for i in range(n):
    age, name =  sys.stdin.readline().split()
    array.append([int(age), i, name])

#print(array)
array.sort()

for i in range(n):
    print(array[i][0], end=" ")
    print(array[i][2])