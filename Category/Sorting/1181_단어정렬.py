import sys
n = int(sys.stdin.readline())

a = []
for i in range(n):
    word = sys.stdin.readline().rstrip()
    a.append(word)
    #array.append([len(word), word])

a = list(set(a))

array = []
for i in range(len(a)):
    array.append([len(a[i]), a[i]])

array.sort()
#print(array)

for i in range(len(a)):
    print(array[i][1])