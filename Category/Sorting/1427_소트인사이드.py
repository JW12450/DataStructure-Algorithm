import sys

n = input()

array = []
for i in range(len(n)):
    array.append(int(n[i]))

array.sort(reverse=True)

for value in array:
    print(value,end="")