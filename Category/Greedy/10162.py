n = int(input())

time = [300, 60, 10]

count = 0
array = [0 for i in range(3)]
for i in range(3):
    count += n//time[i]
    array[i] = n//time[i]
    n = n%time[i]
    if (n == 0):
        break

if (n >0):
    print(-1)
else:
    print(array[0],array[1],array[2])