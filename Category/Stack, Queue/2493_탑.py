import sys

n = int(sys.stdin.readline())
tower = list(map(int, sys.stdin.readline().rstrip().split()))
#스택의 탑은 주어진 인풋중에 통신이 우선순위가 가장 높은 타워의 인덱스
stack = []
ans = []
for i, t in enumerate(tower):
    #해당 차례의 인풋 타워에 대해, 스택의 탑이 현재 탑보다 낮은 경우에는 pop하고, 이를 스택이 빌때까지 반복
    while stack and tower[stack[-1]] < t:
        stack.pop()
    # 통신 가능한 타워가 있는 경우 스택의 탑 인덱스를 정답에 추가
    if stack:
        ans.append(stack[-1]+1)
    # 통신이 가능한 타워가 없는 상황이므로 0
    else:
        ans.append(0)
    stack.append(i)
print(" ".join(map(str, ans)))

"""
#메모리 초과
import sys

n = int(sys.stdin.readline())
tower = list(map(int, sys.stdin.readline().rstrip().split()))
#스택의 탑은 주어진 인풋중에 통신이 우선순위가 가장 높은 아이
stack = []
ans = [0]
for i, t in enumerate(tower):
    #첫번째 탑은 넣고 시작
    if i == 0:
        stack.append((t,i+1))
        continue

    top = stack[-1]
    #스택의 탑이 현재 타워보다 낮으면, 현재 타워가 스택의 탑보다 우선순위를 가지므로 스택 갱신
    if top[0] < t:
        stack.pop()
        stack.append((t,i+1))
        #현재 타워를 기준으로 스택의 뒤에서부터 스캔
        check = False
        for j in range(len(stack)-1, -1, -1):
            if stack[j][0] > t:
                ans.append(stack[j][1])
                check = True
        if not check:
            ans.append(0)
    #스택의 탑이 현재 타워보다 높으면, 둘다 고려해야할수 있기 때문에 현재 타워도 푸시
    elif top[0] > t:
        stack.append((t,i+1))
        #스택의 탑이 현재 타워와 가장먼저 통신함
        ans.append(top[1])

print(" ".join(map(str, ans)))
"""