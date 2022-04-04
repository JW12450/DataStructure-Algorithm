import sys

n = int(sys.stdin.readline())
room = []
for _ in range(n):
    room.append(list(map(int, sys.stdin.readline().split())))

room = sorted(room, key=lambda x:(x[1],x[0]))
print(room)
cur = room[0][1]
cnt = 1
for i in range(1,len(room)):
    if room[i][0] >= cur:
        cur = room[i][1]
        cnt += 1

print(cnt)