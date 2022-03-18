import sys
read = sys.stdin.readline

N, K = map(int, read().split())
bag = [0] * (K+1)

for _ in range(N):
    w, v = map(int, read().split())
    for j in range(K, w-1, -1):
        bag[j] = max(bag[j], bag[j-w] + v)
print(bag[-1])
