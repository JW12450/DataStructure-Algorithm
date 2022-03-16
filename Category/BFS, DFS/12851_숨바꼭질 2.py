import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
time = [-1] * (100001)

def bfs():
    global cnt
    queue = deque()
    queue.append(n)
    time[n] = 0

    while queue:
        x = queue.popleft()
        if x == k:
            cnt += 1
        for nx in (x-1, x+1, 2*x):
            if 0 <= nx <= 100000 :
                if time[nx] == -1 or time[nx] >= time[x]+1:# and not time[nx]:
                    time[nx] = time[x] + 1
                    queue.append(nx)

cnt = 0
bfs()
print(time[k])
print(cnt)
