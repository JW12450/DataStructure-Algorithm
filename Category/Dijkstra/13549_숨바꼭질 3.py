import sys
from collections import deque


n, k = map(int, sys.stdin.readline().split())
time = [9999999] * (100001)

queue = deque()
queue.append(n)
time[n] = 0
while queue:
    #print(queue)
    x = queue.popleft()
    if x == k:
        print(time[x])
        break
    for nx in (x-1, x+1):
        if 0 > nx or nx >100000:
            continue
        if time[nx] > time[x]+1:
            time[nx] = time[x]+1
            queue.append(nx)
    nx = 2 * x
    if 0 <= nx <= 100000 and time[nx] > time[x]:
        time[nx] = time[x]
        queue.append(nx)



