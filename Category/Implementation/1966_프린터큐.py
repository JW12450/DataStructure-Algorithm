import sys
from collections import deque

n = int(sys.stdin.readline())

def solution():
    num_doc, target = map(int, sys.stdin.readline().split())
    priority = list(map(int, sys.stdin.readline().split()))

    pq = []
    for i in range(num_doc):
        pq.append([priority[i], i])

    pq = deque(pq)
    #print(pq)
    #print(max(pq)[0])
    count = 1
    while True:
        if pq[0][0] < max(pq)[0] or (pq[0][0] == max(pq)[0] and pq.count(max(pq)[0] > 1)):
            save = pq.popleft()
            pq.append(save)
        else:
            if pq[0][1] == target:
                print(count)
                break
            else:
                pq.popleft()
                count +=1

for i in range(n):
    solution()