num = int(input())

array = []
for i in range(num):
    array.append(int(input()))

array.sort()

for j in range(num):
    print(array[j])