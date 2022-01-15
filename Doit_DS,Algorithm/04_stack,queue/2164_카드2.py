import sys
from collections import deque

n = int(sys.stdin.readline())

deque = deque([i for i in range(1,n+1)])

while len(deque) >1:
    deque.popleft()
    deque.append(deque.popleft())


print(deque[0])