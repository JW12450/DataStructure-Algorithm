import copy

n, k = map(int, input().split())

af = list(input())
a = []
for x in af:
    a.append(int(x))

#스택의 제일 위의 값과 넣을 값을 비교하며 넣을 값이 클 경우 스택의 제일 위의 값을 제거
stack = []
delnum = k
for i in range(n):
    while delnum>0 and stack:
        print(stack)
        if stack[-1] < a[i]:
            stack.pop()
            delnum -= 1
        else:
            break
    stack.append(a[i])
    print(stack)

for i in range(n-k):
    print(stack[i],end="")

"""
#완전 탐색 시간초과....

#print(a)
#k개의 수를 제거함
for i in range(k):
    cand = []
    for j in range(len(a)):
        ca = copy.deepcopy(a)
        ca.pop(j)
        cand.append(int("".join(map(str,ca))))
    ans = max(cand)
    #print(cand)
    #print(ans)
    a = list(str(ans))

print(ans)

for i in range(k):
    t1 = copy.deepcopy(a)
    t2 = copy.deepcopy(a)
    #print(a_copy)
    t1.pop(0)
    t2.remove(min(t2))
    print(a, int("".join(map(str,t1))), int("".join(map(str,t2))))
    if int("".join(map(str,t1))) > int("".join(map(str,t2))):
        a.pop(0)
    else:
        a.remove(min(a))

print(a)
"""




