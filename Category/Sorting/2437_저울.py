import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().rstrip().split()))

array.sort()
#여태까지의 추의 합이 다음 배열의 요소보다 작으면 해당 합 + 1은 나올수가 없음
target = 0

for i in range(len(array)):
    if target + 1 >= array[i]:
        target += array[i]
    else:
        break

print(target+1)