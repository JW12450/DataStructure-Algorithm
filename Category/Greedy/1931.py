n = int(input())
"""
room_list = [0 for i in range(100000)]
count_list = [0 for i in range(100000)]

for _ in range(n):
    start, end = map(int, input().split())
    j = 0
    while True:
        if (room_list[j] <= start):
            room_list[j] = end
            count_list[j] += 1
            break
        j +=1

print(max(count_list))
"""
tmp = 0
count = 0
for _ in range(n):
    start, end = map(int, input().split())
    if (start >= tmp):
        tmp = end
        count += 1

print(count)