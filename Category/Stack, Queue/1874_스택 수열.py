import sys
n = int(sys.stdin.readline())

stack = []
ans = []
cur = 1
check = True

for _ in range(n):
    target = int(sys.stdin.readline())
    #타켓값이 나올때까지 우선 스택에 push
    while cur <= target:
        stack.append(cur)
        ans.append("+")
        cur += 1
    #스택의 탑이 타겟인지 확인
    if stack[-1] == target:
        stack.pop()
        ans.append("-")
    #스택의 탑이 타겟이 아니면 스택의 구조상 절대 만들어질수 없음
    else:
        check = False
        break

if check:
    for a in ans:
        print(a)
else:
    print("NO")