from collections import deque

n, k = map(int, input().split())

queue = deque([i for i in range(1, n+1)])

print("<",end="")
count = 0
while count < n-1:
    for i in range(k-1):
        queue.append(queue.popleft())
    print(queue.popleft(),end="")
    print(", ",  end="")
    count+=1

print(queue.popleft(), end="")
print(">")