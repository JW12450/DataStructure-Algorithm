import sys, heapq
n , k = map(int, sys.stdin.readline().split())

friend = []
for _ in range(n):
    friend.append(int(sys.stdin.readline()))

q = []
for i in range(1,n):
    heapq.heappush(q, friend[i]- friend[i-1])

ans = 1
#n-k번동안은 차이값만큼을 그래도 켜줘야 이어짐
for i in range(n-k):
    ans += heapq.heappop(q)

ans += len(q)
print(ans)

