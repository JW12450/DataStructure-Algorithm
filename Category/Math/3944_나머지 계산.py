import sys

t = int(sys.stdin.readline())
for _ in range(t):
    b, d = sys.stdin.readline().split()
    b = int(b)
    mod = 0

    for n in d:
        mod += int(n, b) % (b-1)
    print(mod%(b-1))
