"""
import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().rstrip().split()))
#차례로 +, -, *, //
operator = list(map(int, sys.stdin.readline().rstrip().split()))

maximum = -987654321
minimum = 987654321

def dfs(depth, total, plus, minus, multiply, divide):
    global minimum, maximum

    if depth == n:
        maximum = max(maximum, total)
        minimum = min(minimum, total)

    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)

dfs(1, num[0], operator[0], operator[1], operator[2], operator[3])

print(maximum)
print(minimum)
"""

import sys
from itertools import permutations

input = sys.stdin.readline
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().rstrip().split()))
op_num = list(map(int, sys.stdin.readline().rstrip().split()))  # +, -, *, /
op_list = ['+', '-', '*', '/']
op = []

for k in range(len(op_num)):
    for i in range(op_num[k]):
        op.append(op_list[k])

maximum = -987654321
minimum = 987654321


def solve():
    global maximum, minimum
    #모든 순열에 대해 완전탐색
    for p in permutations(op, n - 1):
        total = num[0]
        for r in range(1, n):
            if p[r - 1] == '+':
                total += num[r]
            elif p[r - 1] == '-':
                total -= num[r]
            elif p[r - 1] == '*':
                total *= num[r]
            elif p[r - 1] == '/':
                total = int(total / num[r])

        if total > maximum:
            maximum = total
        if total < minimum:
            minimum = total


solve()
print(maximum)
print(minimum)