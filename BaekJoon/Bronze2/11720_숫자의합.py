n = int(input())

array = list(input())
for i in range(n):
    array[i] = int(array[i])
print(sum(array))