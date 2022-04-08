import sys
from collections import deque

t = int(sys.stdin.readline())
"""시간초과
for _ in range(t):
    p_list = list(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline())
    dq = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    er_check = False
    for p in p_list:
        #R은 뒤집기 함수
        if p == 'R':
            dq.reverse()

        #D는 버리기 함수 + 배열이 비어있는 경우 에러
        else:
            if len(dq) == 0:
                er_check = True
                break
            else:
                dq.popleft()

    if er_check:
        print("error")
    else:
        print("[" + ",".join(dq) + "]")
"""
for _ in range(t):
    p_list = list(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline())
    dq = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    if n == 0:
        dq = deque([])
    er_check = False
    cnt = 0
    #리스트를 뒤집는 횟수를 누적해서 홀수면 reverse, 짝수면 그대로
    for p in p_list:
        #R은 뒤집기 함수
        if p == 'R':
            cnt += 1
        #D는 버리기 함수(cnt값을 보고 pop, popleft 결정) + 배열이 비어있는 경우 에러
        else:
            if len(dq) == 0:
                er_check = True
                break
            else:
                #짝수면 정방향인 상태이므로 popleft
                if cnt % 2 == 0:
                    dq.popleft()
                #홀수면 역방향이므로 Pop
                else:
                    dq.pop()

    if cnt % 2 != 0:
        dq.reverse()
    if er_check:
        print("error")
    else:
        print("[" + ",".join(dq) + "]")




















