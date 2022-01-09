"""
room_list = [0 for i in range(100000)]
count_list = [0 for i in range(100000)]

for i in range(n):
    start, end = map(int, input().split())
    j = 0
    while True:
        if (room_list[j] <= start):
            room_list[j] = end
            count_list[j] += 1
            break
        j +=1

print(max(count_list))
#시간 초과... sys 써보자

import sys

#n = int(input())
n = int(sys.stdin.readline())

array = [[0]*2 for _ in range(n)]

for i in range(n):
    start, end = map(int, sys.stdin.readline().split())
    array[i][0] = start
    array[i][1] = end

sorted(array, key=lambda x: (x[1], x[0]))


cnt = 1
end_time = array[0][1]
for i in range(1, n):
    if array[i][0] >= end_time:
        cnt += 1
        end_time = array[i][1]

print(cnt)
"""

import sys
N = int(sys.stdin.readline())

time = [[0]*2 for _ in range(N)]

for i in range(N):
    s, e = map(int, sys.stdin.readline().split())
    time[i][0] = s
    time[i][1] = e

time.sort(key = lambda x: (x[1], x[0]))

cnt = 1
end_time = time[0][1]

for i in range(1, N):
    if time[i][0] >= end_time:
        cnt += 1
        end_time = time[i][1]

print(cnt)
