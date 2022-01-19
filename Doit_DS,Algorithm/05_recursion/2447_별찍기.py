import sys, math

n = int(sys.stdin.readline())

def recur_star(n):
    if n == 1:
        print("***")
        print("* *")
        print("***")
    if n > 1:
        recur_star(n/3)

print(recur_star(n))