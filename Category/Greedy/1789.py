n = int(input())

count = 0
i = 1
while True:
    n -= i
    if (n == 0):
        count +=1
        break
    if (n <= i):
        n += i
        i += 1
        continue
    i +=1
    count +=1

print(count)



