import sys

n = int(input())
k = int(input())
if k>= n:
    print(0)
    sys.exit()

sensor = list(map(int, input().split()))
sensor.sort()

dif = []
for i in range(len(sensor)-1):
    dif.append(sensor[i+1] - sensor[i])


dif.sort(reverse=True)

for i in range(k-1):
    dif.pop(0)

print(sum(dif))