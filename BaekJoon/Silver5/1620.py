import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

p_dict = {}
for i in range(1,n+1):
    name = sys.stdin.readline().rstrip()
    p_dict[name] = i
    p_dict[str(i)] = name

for i in range(m):
    input = sys.stdin.readline().rstrip()
    print(p_dict[input])
