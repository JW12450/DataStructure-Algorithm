def self_num(n):
    sum = n
    n = str(n)
    for i in range(len(n)):
        sum += int(n[i])
    return sum

i = 1
a1 = [i for i in range(1, 10000)]
array = []
while True:
    if (self_num(i) >= 100000):
        break
    array.append(self_num(i))
    i += 1

ans = []
for i in range(len(a1)):
    if (a1[i] not in array):
        #ans.append(a1[i])
        print(a1[i])
