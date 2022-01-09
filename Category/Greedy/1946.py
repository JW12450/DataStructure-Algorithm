import sys
"""
num_testcase = int(sys.stdin.readline())

def check():
    num = int(input())
    t1 = []
    t2 = []

    index_a = 0
    index_b = 0

    for i in range(num):
        a, b = map(int,sys.stdin.readline().split())
        if a == 1:
            index_a = i
        if b == 1:
            index_b  = i
        t1.append(a)
        t2.append(b)

    point_a = t2[index_a]
    point_b = t1[index_b]

    count = 0
    for i in range(num):
        if t1[i] <= point_b and t2[i] <= point_a :
            count += 1

    return count

ans = []
for i in range(num_testcase):
    ans.append(check())

for i in range(num_testcase):
    print(ans[i])

"""

num_testcase = int(sys.stdin.readline())

for i in range(num_testcase):
    Cnt = 1
    people = []

    N = int(input())
    for i in range(N):
        Paper, Interview = map(int, sys.stdin.readline().split())
        people.append([Paper, Interview])

    people.sort()
    max = people[0][1]
    for i in range(1, N):
        if people[i][1] < max:
            Cnt += 1
            max = people[i][1]

    print(Cnt)