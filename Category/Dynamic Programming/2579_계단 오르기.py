import sys

n = int(sys.stdin.readline())
stairs=[0 for i in range(301)]
for i in range(n):
    stairs[i] = int(sys.stdin.readline().rstrip())

d = [0]*301

d[0] = stairs[0]
d[1] = stairs[0]+stairs[1]
d[2] = max(stairs[1]+stairs[2], stairs[0]+stairs[2])
for i in range(3,n):
    d[i] = max(d[i-3]+stairs[i-1]+stairs[i], d[i-2]+stairs[i])

#print(d)
print(d[n-1])