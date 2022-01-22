import sys

n = int(sys.stdin.readline())

stack = []

for i in range(n):
    input = int((sys.stdin.readline()))

    if input == 0:
        stack.pop()
    else:
        stack.append(input)

print(sum(stack))